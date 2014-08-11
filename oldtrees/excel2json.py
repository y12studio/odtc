#!/usr/bin/env python
#coding:UTF-8
#
#  sudo easy_install xlrd
#
import urllib2,json,csv,xlrd, datetime,io,shutil

url = "http://data.taichung.gov.tw/GipOpenWeb/wSite/public/data/f1406681238639.xlsx"
i = datetime.datetime.now()
prefix = i.strftime("%Y%m%d-%H%M%S")

def csv_from_excel_sheet(file_contents):
	workbook = xlrd.open_workbook(file_contents=file_contents)
	all_worksheets = workbook.sheet_names()
	root={}
	root["name"]="臺中市受保護樹木公告清單"
	root["col"]=["行政區","序號","樹木編號","樹種","座落","地點"]
	rl=[]
	root["csv"]=rl
	for worksheet_name in all_worksheets:
		worksheet = workbook.sheet_by_name(worksheet_name)
		filename = "SHEET%d-T%s.csv"%(len(rl),prefix)
		filename_latest = "SHEET%d-latest.csv"%len(rl)
		your_csv_file = open(filename, 'wb')
		wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
		for rownum in xrange(worksheet.nrows):
			wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])
		your_csv_file.close()
		shutil.copyfile(filename, filename_latest)
		r = {}
		r['name']=worksheet_name
		r['file']=filename
		r['nrows']=worksheet.nrows
		rl.append(r)
	jr = json.dumps(root, indent=4,ensure_ascii=False,encoding='utf8')
	with io.open("RT%s.json"%prefix, 'w', encoding='utf8') as fr:
		fr.write(jr)
		print(jr)
	return root
def main():
	file_contents = urllib2.urlopen(url).read()
	csv_from_excel_sheet(file_contents)
main()

