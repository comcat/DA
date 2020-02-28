#!/usr/bin/env python

import pandas as pd
from scipy import stats

t1 = pd.read_csv('../data/da02-temp-0948.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t2 = pd.read_csv('../data/da02-temp-0019.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t3 = pd.read_csv('../data/da02-temp-1144.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

print(stats.pearsonr(t1['Temp'], t2['Temp']))
#(0.6645110453498703, 2.134012282722948e-09)

print(stats.pearsonr(t1['Temp'], t3))
#(0.057569362179313834, 0.6513750312139728)

print(stats.pearsonr(t2['Temp'], t3))
#(0.07144298994314577, 0.5747996511588451)

