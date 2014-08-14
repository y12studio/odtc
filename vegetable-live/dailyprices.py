#!/usr/bin/env python
#coding:UTF-8
"""
    Market Daily Prices Report at Taipei Market no.109
    ==================================================
    :copyright: 2014 by y12.tw
    :license: Apache Sotware License, see LICENSE for details.
"""
import requests, re, json, os, collections,datetime
os.environ['TZ'] = 'ROC'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2' }
t = datetime.date.today()
data = {'myy':'%d' % (t.year-1911),'mmm':'%02d' % t.month,'mdd':'%02d' % t.day,'mkno':'109','mknoname':'%A5x%A5_%A4%40','B1':'%B6%7D%A9l%ACd%B8%DF'}
html = requests.post('http://amis.afa.gov.tw/v-asp/v107r.asp', verify=False, headers=headers, data=data)
html.encoding='big5'
x = html.text
preTxt = re.findall(u'<pre>.*</pre>',x,re.DOTALL)[0]

# preTxtArr = preTxt.split(u'\r\n\r\n');
# 中文全形空白 　 注意
preTxtArr = re.compile(u"\r\n　?\r\n").split(preTxt)
sarr = sorted(preTxtArr, key=lambda x:x.count(' '), reverse=True)[:3]
rawdata={}
for s in sarr:
	# remove 中文全形空白
	s2 = s.replace(u'　',' ')
	arr2 = s2.split('\r\n')
	if u'花果類' in s2:rawdata['fruit']=arr2
	if u'根莖類' in s2:rawdata['rootveg']=arr2
	if u'葉菜類' in s2:rawdata['vegetable']=arr2
rawdata2={'title':'Fruit,Vegetable Market Daily Prices',
	'homepage':'https://github.com/y12studio/odtc','license':'http://creativecommons.org/about/cc0','time':t.isoformat(),
	'desc':'Market Daily Prices Report at Taipei Market no.109','collections':[]}
for k,v in rawdata.items():
	rlist=[]
	rawdata2['collections'].append({'type':k, 'prices':rlist})
	for line in v:
		varr = line.split()
		if len(varr)==5 and varr[2].isdigit():
			xx = {'id':varr[0],'name':varr[1],'tday':int(varr[2]),'yday':int(varr[3])}
			rlist.append(xx)
print(json.dumps(rawdata2, ensure_ascii=False,indent=4).encode('utf8'))

