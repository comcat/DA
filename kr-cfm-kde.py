#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

plt.figure(figsize=(12,40))

uk = pd.read_csv("./data/covid-19-who/kr.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

ukn = uk['New Confirmed']

l = len(ukn)

i = np.arange(l-1, -1, -1)

ukn.index = i

xtk = np.arange(0, l+10, 5)
xlb = pd.date_range('2020-01-21', periods=l+10, freq='1d')
xlb = xlb.strftime('%m-%d')
ii = []
for ix in xtk:
	ii.append(xlb.values[ix])

#################################
host = host_subplot(111)

#par = host.twinx()

plt.title('New confirmed cases of South Korea\n', {'fontsize':12, 'color': '#222222', 'verticalalignment':'top'})

#par.bar(ukn.index, ukn.values, alpha=0.6, color='#0099cc', label='Confirmed')

#x = ukn.index.repeat(ukn)
#h1 = len(x)**(-1.0/5.0) + 0.00
#h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.35 - 0.3
#px = pd.Series(x)
#px.plot.kde(bw_method=h1, color='#0fa1d3', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
#px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9, alpha=0.9)
host.bar(ukn.index, ukn.values, alpha=0.6, color='#0099cc', label='Confirmed')

#host.set_ylim(ymin=0, ymax=0.0725)
#host.set_ylabel('Probability (Today / Total)', {'fontsize':9, 'color': '#222222'})
host.set_ylabel('Number of new cases')
#par.set_ylabel('Number of cases')

plt.xlim(xmin=0, xmax=55)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)
 
plt.show()
