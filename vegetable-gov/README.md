## link

* [農產品交易行情 | 政府資料開放平臺](http://data.gov.tw/node/8066)
* [行政院農業委員會資料開放平台](http://data.coa.gov.tw/Query/ServiceDetail.aspx?id=037)
* [歡迎光臨農產品交易行情站](http://amis.afa.gov.tw/)

## parse json

```
蔬菜
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=V

水果
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=T

花卉
POST http://amis.afa.gov.tw/imisg1/product_find_proc.asp
product_kind=L

$python veg-type-parse.py -t T > veg-type-t.json
$python veg-type-parse.py -t V > veg-type-v.json
$python veg-type-parse.py -t L > veg-type-l.json

```

## log

Wed Oct 15 10:04:38 CST 2014

```
$ wget http://m.coa.gov.tw/OpenData/FarmTransData.aspx?EndDate=103.09.26 -O test/raw-all-103-09-26.json
$ du -sh test/raw-all-103-09-26.json
1.2M    test/raw-all-103-09-26.json
$ wget 'http://m.coa.gov.tw/OpenData/FarmTransData.aspx?StartDate=103.10.14&EndDate=103.10.14' -O test/raw-all-103-10-14.json
$ du -sh test/raw-all-103-10-14.json
604K    test/raw-all-103-10-14.json
----------------------------------------------------------------------
Ran 4 tests in 0.143s

OK
```

raw1.json

```
$ wget http://m.coa.gov.tw/OpenData/FarmTransData.aspx -O raw1.json
$ cat raw1.json
 [{ "交易日期":"103.08.16","作物代號":"11","作物名稱":"椰子","市場代號":"104","市場名稱":"台北二",
    "上價":"55","中價":"32.4","下價":"16.4","平均價":"33.7","交易量":"825"}...
```
