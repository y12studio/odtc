#!/usr/bin/env python
#coding:UTF-8
"""
    Market Daily Prices From open.gov.tw
    ====================================
    :copyright: 2014 by y12.tw
    :license: Apache Sotware License, see LICENSE for details.	
	Data example :
	{"交易日期":"103.08.16","作物代號":"11","作物名稱":"椰子","市場代號":"104","市場名稱":"台北二","上價":"55","中價":"32.4","下價":"16.4","平均價":"33.7","交易量":"825"}
	交易日期、作物代號、作物名稱、市場代號、市場名稱、上價(元/公斤)、中價(元/公斤)、下價(元/公斤)、平均價(元/公斤) 、交易量(公斤)。

"""
import requests, re, json, os, collections,datetime
os.environ['TZ'] = 'ROC'
t = datetime.date.today()

with open('raw1.json') as df:    
    data = json.load(df)

rmap={'title':'Fruit,Vegetable Market Daily Prices',
	'homepage':'https://github.com/y12studio/odtc','license':'http://creativecommons.org/about/cc0','time':t.isoformat(),
	'desc':'Market Daily Prices Report at Taipei Market no.109','collections':{},'stat':{}}
rs=rmap['stat']
rc=rmap['collections']
for s in data:
	if s[u'市場代號'] != u'109':
		continue
	r={}
	#"市場代號":"109"
	id = s[u'作物代號']
	r['name'] = s[u'作物名稱']
	r['avg'] = float(s[u'平均價'])
	r['max'] = float(s[u'上價'])
	r['mean'] = float(s[u'中價'])
	r['min'] = float(s[u'下價'])
	r['volume'] = float(s[u'交易量'])
	rc[id]=r

rs['count']=len(rc)
#savg = sorted(rc.items(), key=lambda x:x[1]['avg'])
rs['avg_sorted']=[x[0] for x in sorted(rc.items(), key=lambda x:x[1]['avg'])]
rs['volume_sorted']=[x[0] for x in sorted(rc.items(), key=lambda x:x[1]['volume'])]
print(json.dumps(rmap, ensure_ascii=False,indent=4).encode('utf8'))
