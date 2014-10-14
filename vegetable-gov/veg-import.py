#!/usr/bin/env python
#coding:UTF-8
import json,os
from elasticsearch import Elasticsearch

class foo():

    def __init__(self):
        self.esindex = "veg_life_gov"
        self.estype = "veg"
        script_dir =os.path.dirname(__file__)
        file_mapping = os.path.join(script_dir, 'mapping.json')
        self.mapping = json.load(open(file_mapping ,'r'),encoding="utf-8")
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def create_index(self):
        self.es.indices.create(index=self.esindex, ignore=400)
        self.es.indices.put_mapping(index=self.esindex,doc_type=self.estype, body=self.mapping)

    def import_item(self, item):
        try:
            #item['id'] = u"%s-%s-%s" % (x['name'],x['county'],x['election_year'])
            r={}
            #"市場代號":"109"
            r['id'] = item[u'作物代號']
            r['name'] = item[u'作物名稱']
            r['avg'] = float(item[u'平均價'])
            r['max'] = float(item[u'上價'])
            r['mean'] = float(item[u'中價'])
            r['min'] = float(item[u'下價'])
            r['volume'] = float(item[u'交易量'])
            self.es.index(index=self.esindex, doc_type=self.estype, body=r)
        except ValueError:
            print("Oops! ValueError:")
            print(json.dumps(item, indent=4,ensure_ascii=False,encoding='utf8'))
