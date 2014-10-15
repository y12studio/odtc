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
