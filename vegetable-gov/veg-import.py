#!/usr/bin/env python
#coding:UTF-8
import json,os,argparse
import datetime as dt
from elasticsearch import Elasticsearch

class VegImport():

    def __init__(self):
        self.esindex = "veg_life_gov"
        self.estype = "veg"
        self.script_dir =os.path.dirname(__file__)
        file_mapping = os.path.join(self.script_dir, 'mapping.json')
        file_typev = os.path.join(self.script_dir, 'veg-type-v.json')
        file_typel = os.path.join(self.script_dir, 'veg-type-l.json')
        file_typet = os.path.join(self.script_dir, 'veg-type-t.json')
        self.mapping = json.load(open(file_mapping ,'r'),encoding="utf-8")
        self.typev = json.load(open(file_typev ,'r'),encoding="utf-8")
        self.typet = json.load(open(file_typet ,'r'),encoding="utf-8")
        self.typel = json.load(open(file_typel ,'r'),encoding="utf-8")
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def test_import(self, raw_json_path):
        rpath = os.path.join(self.script_dir, raw_json_path)
        data = json.load(open(rpath ,'r'),encoding="utf-8")
        for item in data:
            self.import_item(item)


    def create_index(self):
        self.es.indices.create(index=self.esindex, ignore=400)
        self.es.indices.put_mapping(index=self.esindex,doc_type=self.estype, body=self.mapping)

    def import_item(self, item):
        try:
            r={}
            r['pid'] = item[u'作物代號']
            r['market_id'] = item[u'市場代號']
            r['market'] = item[u'市場名稱']
            darr = item[u'交易日期'].split('.')
            r['date'] = dt.date(int(darr[0])+1911, int(darr[1]), int(darr[2]))
            pid = r['pid']
            if pid in self.typev:
                # 蔬菜
                name = self.typev[pid]['name']
                ext = self.typev[pid]['ext']
                if ext == u'進口':
                    r['ptype'] = 'vi'
                else:
                    r['ptype'] = 'v'
                    r['ext'] = ext
                r['name'] = name

            elif pid in self.typel:
                name = self.typel[pid]['name']
                ext = self.typel[pid]['ext']
                # l 花卉無進口欄位
                r['ptype'] = 'l'
                r['ext'] = ext
                r['name'] = name

            elif pid in self.typet:
                # 水果
                ext = self.typet[pid]['ext']
                name = self.typet[pid]['name']
                if ext == u'進口':
                    r['ptype'] = 'ti'
                    # 蘋果富士
                    if u'蘋果' in name:
                        r['name'] = u'蘋果'
                        r['ext'] = name.replace(u'蘋果','')
                    else:
                        r['name'] = name
                else:
                    r['ptype'] = 't'
                    r['ext'] = ext
                    r['name'] = name
            else:
                r['ptype'] = 'x'
            r['name_raw'] = item[u'作物名稱']
            p = {}
            r['price'] = p
            p['avg'] = float(item[u'平均價'])
            p['max'] = float(item[u'上價'])
            p['mean'] = float(item[u'中價'])
            p['min'] = float(item[u'下價'])
            r['volume'] = float(item[u'交易量'])
            itemid = "%s-%s-%s" %(pid,r['market_id'],r['date'])
            self.es.index(index=self.esindex, doc_type=self.estype, id=itemid, body=r)
        except ValueError:
            print("Oops! ValueError:")
            print(json.dumps(item, indent=4,ensure_ascii=False,encoding='utf8'))

def main():
    parser = argparse.ArgumentParser(description='import elasticsearch')
    #parser.add_argument('-i', '--input', help='Input directory', required=True)
    parser.add_argument('-t', '--test', const='FOO', nargs='?', help='Test', required=False)
    args = parser.parse_args()
    # print(args)
    if args.test:
        print("test import")
        vi = VegImport()
        vi.create_index()
        # 103-09-25 and 103-09-26
        # http://m.coa.gov.tw/OpenData/FarmTransData.aspx?EndDate=103.09.26
        # two days
        flist = ['test/raw-all-103-09-25-26.json',
            'test/raw-all-103-10-03.json',
            'test/raw-all-103-10-12.json',
            'test/raw-all-103-10-13.json',
            'test/raw-all-103-10-14.json']
        for f in flist:
            vi.test_import(f)

if __name__ == '__main__':
    main()
