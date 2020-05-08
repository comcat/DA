#!/usr/bin/env python

import pandas as pd
from pandas.tseries.offsets import Day, MonthEnd

import requests

from datetime import datetime

now = datetime.now()
today = datetime(now.year, now.month, now.day)

url = "https://covidtracking.com/api/us/daily?date="

#resp = requests.get(url)
#'{"date":20200317,"states":56,"positive":5723,"negative":47604,"posNeg":53327,"pending":815,"death":90,"total":54085}'
#resp.json()

df = pd.read_csv("us.csv",index_col='Date',parse_dates=True)

last = df.index[-1]
it = last + Day()

# need update the csv
while it <= today:
	resp = requests.get(url+it.strftime('%Y%m%d'))

	if resp.ok:
		d = resp.json()

		if len(d) > 5:
			last_cfm = df.loc[last]['Confirmed']
			last_dea = df.loc[last]['Deaths']
			idx = pd.to_datetime(d['date'],format='%Y%m%d')
			df.loc[idx] = [d['positive'], d['positive']-last_cfm, d['death'], d['death']-last_dea]
			last = df.index[-1]

	it += Day()

#print(df)
df.to_csv("us.csv",date_format='%Y%m%d')
