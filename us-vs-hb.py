#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from mpl_toolkits.axes_grid1 import host_subplot

plt.rcParams['legend.fontsize'] = 'x-large'
plt.rcParams['ytick.labelsize'] = 13

plt.figure(figsize=(14.4,21.6))
#plt.figure(figsize=(11.25,24.36))
 
hb = pd.read_csv("./data/ncp-hb-new.csv", skipinitialspace=True, index_col='Date', parse_dates=True)
us = pd.read_csv("./data/us.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

hbn = hb['Confirmed']
usn = us['New Confirmed']

hbn['2020-02-12'] = 1508	# Lab-confirmed cases, filter the Clinically diagnosed (exception number)

hbn = hbn[:-1]		# start at 2020-01-10 (1/15) vs. start at 2020-02-29 (3/5)
itn = usn[35:]
hb_start_day = '2020-01-10'
it_start_day = '2020-02-27'

hl = len(hbn)
hbn.index = np.arange(hl-1, -1, -1)

il = len(itn)
itn.index = np.arange(0, il, 1)

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

plt.title('New confirmed cases of COVID-19 (United States vs. Hubei)\n', {'fontsize':17, 'fontweight':'bold','color': '#0b0c0c', 'verticalalignment':'top'})

#bns=np.arange(-0.5,l+0.5,1)
#par.hist(x, bins=bns, rwidth=0.9, alpha=0.4)
w = 0.5
# C1, C8 #A7C957
par.bar(hbn.index, hbn.values, width=0.5, alpha=0.3, color='#1d70b8', label='Hubei: '+hb_start_day+'~'+hb_end_day)
par.bar(itn.index+w, itn.values, width=w, alpha=1, color='#d5281b', label='   USA: '+it_start_day+'~'+it_end_day)


x = hbn.index.repeat(hbn)
h1 = len(x)**(-1.0/5.0)
h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.79
px = pd.Series(x)
#px.plot.kde(bw_method=h1, color='C1', label='KDE (h='+str(format(h1,'.2f'))+')', linewidth=0.9, alpha=0.4)
px.plot.kde(bw_method=h2, color='#DFDFE3', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9, alpha=0.3)

# 0.09/5k * 9k
#host.set_ylim(ymin=0, ymax=0.16)

host.set_ylim(ymin=0, ymax=0.09)

host.set_ylabel('Probability (New / Total)',{'fontsize':14})

par.set_ylabel('Number of cases',{'fontsize':14})

XM = int(hl/5) * 5
plt.xlim(xmin=0, xmax=XM)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii,{'fontsize':13, 'alpha':0.5})

ax.annotate('Data Source: The COVID Tracking Project, WHO, China CDC.  Analysis by: Jack Tan',
			xy=(1, 0), xycoords='axes fraction',
            xytext=(0, -116), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
			fontsize=14)

plt.gcf().autofmt_xdate()

# rect = (left,bottom,right,top)
plt.tight_layout(pad=1.6, rect=(0.03,-0.03,0.97,0.96))

plt.legend()
plt.grid(linewidth=0.5,alpha=0.6)

ofname = "export/us-vs-hb-" + it_day_range[il-1].strftime('%m%d') + '.png'

plt.savefig(ofname, dpi=120)
#plt.show()
