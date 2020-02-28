#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
 
hb = pd.read_csv("../data/ncp-hb-new.csv", index_col='Date', parse_dates=True, skipinitialspace=True)
cn = pd.read_csv("../data/ncp-cn-new.csv", index_col='Date', parse_dates=True, skipinitialspace=True)

xhb = cn-hb
xhb_cf = xhb['Confirmed'].values

plt.bar(xhb.index, xhb_cf, align='edge', width=0.3, label='Outside Hubei')
plt.bar(hb.index, hb['Confirmed'].values, align='edge', width=-0.4, label='Hubei')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
