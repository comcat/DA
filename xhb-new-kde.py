#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

#plt.figure(figsize=(12,12))
host = host_subplot(111)
par = host.twinx()
 
hb = pd.read_csv("./data/ncp-hb-new.csv", skipinitialspace=True)
cn = pd.read_csv("./data/ncp-cn-new.csv", skipinitialspace=True)

xhb = cn-hb

xhb = xhb[:-1]		# start at 2020-01-10

plt.title('New cases (Outside Hubei)')

l = len(xhb)
i = np.arange(l-1, -1, -1)

xhb.index = i

x = xhb.index.repeat(xhb['Confirmed']+xhb['Suspected'])

h1 = len(x)**(-1.0/5.0)
h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.35
px = pd.Series(x)
px.plot.kde(bw_method=h1, color='C1', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9)
#px.plot.kde(bw_method=0.3, color='C2')

#bns=np.arange(-0.5,l+0.5,1)
#par.hist(x, bins=bns, rwidth=0.9, alpha=0.4)
par.bar(xhb.index, xhb['Confirmed'].values, alpha=0.4, label='Confirmed')
par.bar(xhb.index, xhb['Suspected'].values, bottom=xhb['Confirmed'].values, alpha=0.4, color='C1', label='Suspected')

host.set_ylim(ymin=0.0002)
host.set_ylabel('Probability (New / Total)')
par.set_ylabel('Number of cases')

plt.xlim(xmin=-5, xmax=50)

xtk = np.arange(0, l, 5)

ax = plt.gca()
ax.set_xticks(xtk)

xlb = pd.date_range('2020-01-10', periods=l+5, freq='1d')
xlb = xlb.strftime('%m-%d')
ii = []
for i in xtk:
	ii.append(xlb.values[i])

ax.set_xticks(xtk)
ax.set_xticklabels(ii)

#ax.set_xticklabels(['01-20', '01-25', '01-30', '02-04', '02-09', '02-14', '02-19'])

#ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d'))
#plt.gcf().autofmt_xdate

plt.xticks(rotation=45)
plt.grid(linewidth=0.5)
plt.legend()
plt.show()
