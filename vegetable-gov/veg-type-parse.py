#!/usr/bin/env python
#coding:UTF-8
import json,os,argparse
import datetime as dt
import requests
from BeautifulSoup import BeautifulSoup
'''
蔬菜
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=V

水果
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=T

花卉
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=L
'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip,deflate,sdch', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2' }

def parse(atype):
    data = {'product_kind':atype}
    html = requests.post('http://amis.afa.gov.tw/imisg1/product_find_proc.asp', verify=False, headers=headers, data=data)
    html.encoding='big5'
    x = html.text
    soup = BeautifulSoup(x)
    table = soup.find("table")
    rows = table.findAll('tr')
    rlist = {}
    for tr in rows:
        tds = [td.text.replace("&nbsp;","").strip() for td in tr.findAll('td')]
        if len(tds)==3:
            r={'name':tds[1],'ext':tds[2]}
            rlist[tds[0]] = r
    print(json.dumps(rlist, ensure_ascii=False,indent=4).encode('utf8'))

def main():
    parser = argparse.ArgumentParser(description='parse veg type')
    #parser.add_argument('-i', '--input', help='Input directory', required=True)
    parser.add_argument('-t', '--type', help='Type', required=True)
    args = parser.parse_args()
    # print(args)
    if args.type:
        #print("parse type %s" % args.type)
        parse(args.type)

if __name__ == '__main__':
    main()
