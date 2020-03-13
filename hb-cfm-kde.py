#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
 
hb = pd.read_csv("./data/ncp-hb-new.csv", skipinitialspace=True)
#cn = pd.read_csv("./data/ncp-cn-new.csv", skipinitialspace=True)

xhb = hb

xhb = xhb[:-11]		# start at 2020-01-20

plt.title('New cases confirmed in Hubei')
#plt.bar(xhb.index, xhb['Confirmed'].values, alpha=0.6)

l = len(xhb)
i = np.arange(l-1, -1, -1)

xhb.index = i

x = xhb.index.repeat(xhb['Confirmed'])

bns = np.arange(-0.5, l+0.5, 1)
plt.hist(x, bins=bns, rwidth=0.9, alpha=0.6, density=True)

h = len(x)**(-1.0/5.0)
px = pd.Series(x)
px.plot.kde(bw_method=h, color='C1')

plt.ylabel('Probability')

plt.xlim(xmin=-5, xmax=40)

xtk = np.arange(0, l, 5)

ax = plt.gca()

#ax.set_xticks(xtk)
#ax.set_xticklabels(['01-20', '01-25', '01-30', '02-04', '02-09', '02-14', '02-19'])

xlb = pd.date_range('2020-01-20', periods=l+5, freq='1d')
xlb = xlb.strftime('%m-%d')
ii = []
for i in xtk:
	ii.append(xlb.values[i])

ax.set_xticks(xtk)
ax.set_xticklabels(ii)


#xlb = pd.date_range('2020-01-20', periods=len(xtk), freq='5d')

#ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))
#ax.autofmt_xdate()

plt.xticks(rotation=45)
plt.grid(linewidth=0.5)
plt.show()
