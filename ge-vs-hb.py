#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

plt.figure(figsize=(12,40))
 
hb = pd.read_csv("./data/ncp-hb-new.csv", skipinitialspace=True, index_col='Date', parse_dates=True)
it = pd.read_csv("./data/covid-19-who/Germany.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

hbn = hb['Confirmed']
itn = it['New Confirmed']

hbn['2020-02-12'] = 1508	# Lab-confirmed cases, filter the Clinically diagnosed (exception number)

hbn = hbn[:-1]		# start at 2020-01-10 (1/15) vs. start at 2020-02-26 (3/2)
itn = itn[:-29]
hb_start_day = '2020-01-10'
it_start_day = '2020-02-26'

#hbn = hbn[:-5]		# start at 2020-01-14 vs. start at 2020-02-22
#itn = itn[:-22]
#start_day = '2020-01-14'

#hbn = hbn[:-7]		# start at 2020-01-16 vs. start at 2020-02-22
#itn = itn[:-22]
#start_day = '2020-01-16'

hl = len(hbn)
hbn.index = np.arange(hl-1, -1, -1)

il = len(itn)
itn.index = np.arange(il-1, -1, -1)

xtk = np.arange(0, hl, 5)
hb_day_range = pd.date_range(hb_start_day, periods=hl+5, freq='1d')
xlb = hb_day_range.strftime('%m-%d')
ii = []
for i in xtk:
	ii.append(xlb.values[i])

it_day_range = pd.date_range(it_start_day, periods=il, freq='1d')
it_start_day = it_day_range[0].strftime('%m/%d')
it_end_day = it_day_range[il-1].strftime('%m/%d')

hb_start_day = hb_day_range[0].strftime('%m/%d')
hb_end_day = hb_day_range[il-1].strftime('%m/%d')

#################################
host = host_subplot(111)
par = host.twinx()

plt.title('New confirmed cases of COVID-19 (Germany vs. Hubei)')

#bns=np.arange(-0.5,l+0.5,1)
#par.hist(x, bins=bns, rwidth=0.9, alpha=0.4)
w = 0.5
# C1, C8 #A7C957
par.bar(hbn.index, hbn.values, width=0.5, alpha=0.95, color='#A7C957', label='Hubei: '+hb_start_day+'~'+hb_end_day)
#par.bar(itn.index+w, itn.values, width=w, alpha=1, color='#FA9500', label='Germany')
par.bar(itn.index+w, itn.values, width=w, alpha=1, color='C1', label='Germany: '+it_start_day+'~'+it_end_day)
#par.bar(itn.index+w, itn.values, width=w, alpha=0.95, color='#BC4749', label='Germany')


x = hbn.index.repeat(hbn)
h1 = len(x)**(-1.0/5.0)
h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.79
px = pd.Series(x)
#px.plot.kde(bw_method=h1, color='C1', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='C2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9, alpha=0.4)

host.set_ylim(ymin=0, ymax=0.09)
host.set_ylabel('Probability (New / Total)')

par.set_ylabel('Number of new confirmed cases')

plt.xlim(xmin=0, xmax=65)

#plt.ylim(ymax=3000)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii)

ax.annotate('Data Source: WHO, China CDC, European Centre of Disease Prevention',
			xy=(1, 0), xycoords='axes fraction',
            xytext=(-10, -80), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
			fontsize=12)

plt.gcf().autofmt_xdate()
#plt.xticks(rotation=45)
plt.legend()
plt.grid(linewidth=0.5)

plt.show()
