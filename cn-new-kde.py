#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

host = host_subplot(111)
par = host.twinx()

cn = pd.read_csv("./data/ncp-cn-new.csv", skipinitialspace=True)

xhb = cn

xhb = xhb[:-1]		# start at 2020-01-10

plt.title('New cases (China)')

l = len(xhb)
i = np.arange(l-1, -1, -1)

xhb.index = i

bns=np.arange(-0.5,l+0.5,1)

#par.hist(x, bins=bns, rwidth=0.9, alpha=0.4)
par.bar(xhb.index, xhb['Confirmed'].values, alpha=0.4, label='Confirmed')
par.bar(xhb.index, xhb['Suspected'].values, bottom=xhb['Confirmed'].values, alpha=0.4, color='C1', label='Suspected')


x = xhb.index.repeat(xhb['Confirmed']+xhb['Suspected'])

h = len(x)**(-1.0/5.0)
px = pd.Series(x)
px.plot.kde(bw_method=h, color='C1', label='KDE')


host.set_ylim(ymin=0, ymax=0.1)
host.set_ylabel('Probability (Today / Total)')
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

plt.xticks(rotation=45)
plt.grid(linewidth=0.5)
plt.legend()
plt.show()
