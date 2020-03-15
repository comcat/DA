#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

plt.figure(figsize=(12,40))

cn = pd.read_csv("./data/ncp-cn-new.csv", index_col='Date', skipinitialspace=True)
hb = pd.read_csv("./data/ncp-hb-new.csv", index_col='Date', skipinitialspace=True)

xhb = cn - hb

xhb = xhb[:-1]		# start at 2020-01-20

l = len(xhb)

i = np.arange(l-1, -1, -1)

xhb.index = i

xtk = np.arange(0, l, 5)
xlb = pd.date_range('2020-01-10', periods=l+5, freq='1d')
xlb = xlb.strftime('%m-%d')
ii = []
for ix in xtk:
	ii.append(xlb.values[ix])


x = xhb.index.repeat(xhb['Confirmed']+xhb['Suspected'])

bns=np.arange(-0.5,l+0.5,1)

#################################
host = host_subplot(111)
par = host.twinx()

plt.title('New cases confirmed (Outside Hubei)', {'fontsize':10, 'color': '#222222'})
x = xhb.index.repeat(xhb['Confirmed'])

#plt.hist(x, bins=bns, rwidth=0.9, alpha=0.4, density=True, color='C8')
par.bar(xhb.index, xhb['Confirmed'].values, alpha=0.6, color='#0099cc', label='Confirmed')

h1 = len(x)**(-1.0/5.0) + 0.00
h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.35 - 0.3
px = pd.Series(x)
px.plot.kde(bw_method=h1, color='#0fa1d3', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9, alpha=0.9)

host.set_ylim(ymin=0, ymax=0.0725)
#host.set_ylim(ymin=0)
host.set_ylabel('Probability (Today / Total)', {'fontsize':9, 'color': '#222222'})
par.set_ylabel('Number of cases')

plt.xlim(xmin=-5, xmax=65)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)
 
plt.show()
