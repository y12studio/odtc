#!/usr/bin/env python
#coding:UTF-8
"""
    Market Daily Prices From open.gov.tw
    ====================================
    :copyright: 2014 by y12.tw
    :license: Apache Sotware License, see LICENSE for details.	
	Data example :
	{"交易日期":"103.08.16","作物代號":"11","作物名稱":"椰子","市場代號":"104","市場名稱":"台北二","上價":"55","中價":"32.4","下價":"16.4","平均價":"33.7","交易量":"825"}
"""
import requests, re, json, os, collections,datetime
os.environ['TZ'] = 'ROC'

with open('raw1.json') as df:    
    data = json.load(df)
print(data[1][u'平均價'])