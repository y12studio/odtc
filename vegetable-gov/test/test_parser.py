#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import json,os
# import time
import unittest
#import requests.exceptions
# from requests import get
from veg import getDateStrings,getDateStringsByMonth,Converter
import datetime as dt
from requests import get
# from requests.exceptions import ConnectionError

def getJson(filename):
    script_dir = os.path.dirname(__file__)
    return json.load(open( os.path.join(script_dir, filename)))

class TestConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def _online(self):
        r = get('http://m.coa.gov.tw/OpenData/FarmTransData.aspx?EndDate=103.09.26')
        self.assertEquals(200,r.status_code)
        jr = r.json()
        self.assertEquals(5428,len(jr))

    def test_daterange(self):
        start_date = dt.date(2014, 9, 1)
        end_date = dt.date(2014, 9, 5)
        r = getDateStrings(start_date,end_date)
        self.assertEquals(5,len(r))
        self.assertEquals('103.09.01',r[0])

    def test_daterange_month(self):
        r = getDateStringsByMonth(2014,1)
        self.assertEquals(31,len(r))
        self.assertEquals('103.01.01',r[0])


    def test_convert(self):
        data = getJson('raw1.json')
        cv = Converter(data)
        self.assertTrue(cv != None)
        rmap = cv.convert_only_market109()
        self.assertTrue(rmap != None)
        self.assertTrue('collections' in rmap)
        self.assertEquals(313, len(rmap['collections']))

    def test_convert2(self):
        data = getJson('raw-all-103-09-26.json')
        self.assertTrue(data != None)
        self.assertEquals(5428, len(data))

if __name__ == "__main__":
    unittest.main()
