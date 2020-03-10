#!/usr/bin/env python

import pdfplumber
import pandas as pd

import sys, getopt

def usage():
	print("Usage: pdf2csv.py -i in_file -o out_file [-s start_page -n page_num]")

if len(sys.argv) < 5:
	usage()
	sys.exit()

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:s:n:")
except getopt.GetoptError:
	usage()
	sys.exit(-1)

ifile = ""
ofile = ""
start_page = 2
page_num = 3

for op, value in opts:
	if op == "-i":
		ifile = value
	elif op == "-o":
		ofile = value
	elif op == "-s":
		start_page = int(value)
	elif op == "-n":
		page_num = int(value)
	elif op == "-h":
		usage()
		sys.exit()

#print("start_page = ", start_page)

#pdf = pdfplumber.open("../../Documents/COVID-19/20200307-sitrep-47-covid-19.pdf")

pdf = pdfplumber.open(ifile)

table_settings = {"vertical_strategy": "lines","horizontal_strategy": "lines","join_tolerance": 3,"snap_tolerance": 6}

df_all = pd.DataFrame()

tab2_cols = list()

for page in range(start_page, start_page+page_num):

	#print(page)
	ta = pdf.pages[page].extract_table(table_settings)
	#tdf[[0,2,5,8,9]].dropna()

	if page == start_page:
		df_tmp = pd.DataFrame(ta[1:], columns=ta[0])

		#df_tmp.columns = [ col_tmp.replace('\n','') for col_tmp in df_tmp.columns ]
		for col_tmp in df_tmp.columns:
			if col_tmp:
				col_tmp.replace('\n','')
				tab2_cols.append(col_tmp)
			else:
				tab2_cols.append(' ')

		tab2_cols = df_tmp.columns
	else:
		df_tmp = pd.DataFrame(ta)
		df_tmp.columns = tab2_cols

	df_tmp.replace(to_replace = r'\n', value = '', regex = True, inplace = True)
	df_tmp.dropna()
	
	df_all = pd.concat([df_all, df_tmp], ignore_index=True)

df_all.to_csv(ofile, header=True, index=False)
