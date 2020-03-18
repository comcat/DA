#!/usr/bin/env python

import pandas as pd
from pandas.tseries.offsets import Day, MonthEnd

import requests

from datetime import datetime

now = datetime.now()
today = datetime(now.year, now.month, now.day)

pre_day = today - Day()
.strftime('%Y%m%d')

url = "https://covidtracking.com/api/us/daily?date="

resp = requests.get(url)
#'{"date":20200317,"states":56,"positive":5723,"negative":47604,"posNeg":53327,"pending":815,"death":90,"total":54085}'
resp.json()


df = pd.read_csv("us.csv",index_col='Date',parse_dates=True)

# need update the csv
if pre_day > df.index[-1]:


df.to_csv("usx.csv")
