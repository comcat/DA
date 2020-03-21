#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

plt.figure(figsize=(12,40))

cn = pd.read_csv("./data/ncp-bj-new.csv", index_col='Date', skipinitialspace=True)

xhb = cn

xhb = xhb[:-1]		# start at 2020-01-19

l = len(xhb)

i = np.arange(l-1, -1, -1)

xhb.index = i

xtk = np.arange(0, l, 5)
xlb = pd.date_range('2020-01-19', periods=l+5, freq='1d')
xlb = xlb.strftime('%m-%d')
ii = []
for ix in xtk:
	ii.append(xlb.values[ix])


x = xhb.index.repeat(xhb['Confirmed']+xhb['Suspected'])

bns=np.arange(-0.5,l+0.5,1)

#################################
host = host_subplot(311)
par = host.twinx()

plt.title('New cases confirmed (Beijing)', {'fontsize':10, 'color': '#222222'})
x = xhb.index.repeat(xhb['Confirmed'])

#plt.hist(x, bins=bns, rwidth=0.9, alpha=0.4, density=True, color='C8')
par.bar(xhb.index, xhb['Confirmed'].values, alpha=0.6, color='#0099cc', label='Confirmed')

h1 = len(x)**(-1.0/5.0) - 0.15
#h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0)
h2 = 0.43
px = pd.Series(x)
px.plot.kde(bw_method=h1, color='#0fa1d3', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9)

#host.set_ylim(ymin=0.0002)
host.set_ylim(ymin=0, ymax=0.082)
host.set_ylabel('Probability (Today / Total)', {'fontsize':9, 'color': '#222222'})
par.set_ylabel('Number of cases')

plt.xlim(xmin=-15, xmax=60)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)
 
#################################
host = host_subplot(312)
par = host.twinx()

plt.title('New cases suspected (Beijing)', color='#222222', fontsize=10)
x = xhb.index.repeat(xhb['Suspected'])

#plt.hist(x, bins=bns, rwidth=0.9, alpha=0.7, density=True, color='C1')
par.bar(xhb.index, xhb['Suspected'].values, alpha=0.6, color='C8', label='Suspected')

#h1 = len(x)**(-1.0/5.0)
#h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.55
h1 = 0.13
h2 = 0.43
px = pd.Series(x)
px.plot.kde(bw_method=h1, color='C8', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9)

host.set_ylim(ymin=0, ymax=0.14)
host.set_ylabel('Probability (Today / Total)', {'fontsize':9, 'color': '#222222'})
par.set_ylabel('Number of cases')

plt.xlim(xmin=-15, xmax=60)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)

#################################
host = host_subplot(313)
par = host.twinx()

host.set_title('New cases Confirmed+Suspected (Beijing)', color='#222222', fontsize=10)
x = xhb.index.repeat(xhb['Confirmed']+xhb['Suspected'])

#plt.hist(x, bins=bns, rwidth=0.9, alpha=0.4, density=True, color='C2')
par.bar(xhb.index, xhb['Confirmed'].values, alpha=0.5, label='Confirmed', color='C0')
par.bar(xhb.index, xhb['Suspected'].values, bottom=xhb['Confirmed'].values, alpha=0.6, color='C8', label='Suspected')

#h1 = len(x)**(-1.0/5.0)
#h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.35
h1 = 0.15
h2 = 0.43
px = pd.Series(x)
px.plot.kde(bw_method=h1, color='C1', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9)


host.set_ylim(ymin=0, ymax=0.08)
host.set_ylabel('Probability (Today / Total)', {'fontsize':9, 'color': '#222222'})
par.set_ylabel('Number of cases')

plt.xlim(xmin=-15, xmax=60)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)
plt.show()
