#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pandas.tseries.offsets import Day, MonthEnd

import requests, sys, getopt

from datetime import datetime

def usage():
	print("Usage: update-euro.py [-d day]")

if len(sys.argv) == 1:
	now = datetime.now()
	today = datetime(now.year, now.month, now.day)
else:
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hd:")
	except getopt.GetoptError:
		usage()
		sys.exit(-1)
	
	for op, value in opts:
		if op == "-d":
			today = value
		elif op == "-h":
			usage()
			sys.exit()


files = ['Germany.csv', 'France.csv', 'Italy.csv', 'uk.csv', 'Spain.csv']

#td.loc['United States of America']
#td.loc['France']
#td.loc['Germany']
#td.loc['Italy'][:-2]
#Total confirmed‡ cases        31506
#Total confirmed new cases1     3526
#Total deaths                   2503
#Total new deaths1               345
#>>> x = td.loc['Italy'][:-2]
#>>> type(x)
#<class 'pandas.core.series.Series'>
#>>> last = it.index[0]
#>>> from pandas.tseries.offsets import Day
#>>> last += Day()
#Timestamp('2020-03-20 00:00:00')
#>>> it.loc[last] = x
#it.sort_index(ascending=False, inplace=True)

def update_one(csv, cty):
	df = pd.read_csv("covid-19-who/"+csv, index_col='Date', parse_dates=True)

	last = df.index[0]
	idx = last

	# need update the csv
	while idx < today:

		fname = idx.strftime('%Y%m%d') + '-outside-cn.csv'

		try:
			wd = pd.read_csv("covid-19-who/"+fname, index_col='Reporting Country/ Territory/Area†')
		except IOError:
			print(fname+" is not exist")
			idx += Day()
			continue

		if cty == 'ge':
			x = wd.loc['Germany'][:-2]
		elif cty == 'fr':
			x = wd.loc['France'][:-2]
		elif cty == 'it':
			x = wd.loc['Italy'][:-2]
		elif cty == 'uk':
			x = wd.loc['The United Kingdom'][:-2]
		elif cty == 'sp':
			x = wd.loc['Spain'][:-2]

		x = np.int32(x.values)

		if len(x) == 4:

			df.loc[idx] = x

		else:
			print(idx.strftime('%Y%m%d') + " data is invalid")

		idx += Day()

	df.sort_index(ascending=False, inplace=True)
	#print(df)
	df.to_csv("covid-19-who/"+csv, date_format='%Y%m%d')

update_one("uk.csv", 'uk')
update_one("France.csv", 'fr')
update_one("Germany.csv", 'ge')
update_one("Italy.csv", 'it')
update_one("Spain.csv", 'sp')
