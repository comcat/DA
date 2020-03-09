#!/usr/bin/env python

import pdfplumber
import pandas as pd

pdf = pdfplumber.open("../../Documents/COVID-19/20200307-sitrep-47-covid-19.pdf")

table_settings = {"vertical_strategy": "lines","horizontal_strategy": "lines","join_tolerance": 3,"snap_tolerance": 6}

df_all = pd.DataFrame()

tab2_cols = list()

for page in range(2,5):

	#print(page)
	ta = pdf.pages[page].extract_table(table_settings)
	#tdf[[0,2,5,8,9]].dropna()

	if page == 2:
		df_tmp = pd.DataFrame(ta[1:], columns=ta[0])
		df_tmp.columns = [ col_tmp.replace('\n','') for col_tmp in df_tmp.columns ]
		tab2_cols = df_tmp.columns
	else:
		df_tmp = pd.DataFrame(ta)
		df_tmp.columns = tab2_cols

	df_tmp.replace(to_replace = r'\n', value = '', regex = True, inplace = True)
	df_tmp.dropna()
	
	df_all = pd.concat([df_all, df_tmp], ignore_index=True)

df_all.to_csv('who-0307.csv', header=True, index=False)
