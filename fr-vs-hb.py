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
it = pd.read_csv("./data/covid-19-who/France.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

hbn = hb['Confirmed']
itn = it['New Confirmed']

hbn['2020-02-12'] = 1508	# Lab-confirmed cases, filter the Clinically diagnosed (exception number)

hbn = hbn[:-1]		# start at 2020-01-10 (1/15) vs. start at 2020-02-22 (2/27)
itn = itn[:-31]
hb_start_day = '2020-01-10'
it_start_day = '2020-02-25'

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

plt.title('New confirmed cases of COVID-19 (France vs. Hubei)\n', {'fontsize':17, 'fontweight':'bold','color': '#0b0c0c', 'verticalalignment':'top'})

x = hbn.index.repeat(hbn)
h1 = len(x)**(-1.0/5.0)
h2 = 1.06 * np.std(x) * len(x)**(-1.0/5.0) - 0.79
px = pd.Series(x)
px.plot.kde(bw_method=h2, color='#DFDFE2', label='KDE (h='+str(format(h2,'.2f'))+')', linewidth=0.9, alpha=0.7)

#bns=np.arange(-0.5,l+0.5,1)
#par.hist(x, bins=bns, rwidth=0.9, alpha=0.4)
w = 0.5
# C1, C8 #A7C957
par.bar(hbn.index, hbn.values, width=0.5, alpha=0.8, color='#DFDFE2', label=' Hubei: '+hb_start_day+'~'+hb_end_day)
par.bar(itn.index+w, itn.values, width=w, alpha=0.9, color='#2b92e4', label='France: '+it_start_day+'~'+it_end_day)


ym=0.5
#yl = np.arange(0, ym+0.1, 0.1)
yl = [0,0.1,0.2,0.3,0.4,0.5]

host.set_ylim(ymin=0, ymax=ym)
host.set_yticklabels(yl, {'fontsize':13, 'alpha':0.5})

host.set_ylabel('Probability (New / Total)',{'fontsize':14, 'alpha':0.5})
par.set_ylabel('Number of cases',{'fontsize':14, 'alpha':0.8})

XM = int(hl/5) * 5
plt.xlim(xmin=0, xmax=XM)

ax = plt.gca()
ax.set_xticks(xtk)
ax.set_xticklabels(ii,{'fontsize':13, 'alpha':0.2})

ax.annotate('Data Source: WHO, China CDC, European Centre of Disease Prevention. Analysis by: Jack Tan',
			xy=(1, 0), xycoords='axes fraction',
            xytext=(0, -116), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
			fontsize=14)

plt.gcf().autofmt_xdate()

# rect = (left,bottom,right,top)
plt.tight_layout(pad=1.6, rect=(0.03,-0.03,0.97,0.96))

plt.legend()
plt.grid(linewidth=0.5,alpha=0.3)

ofname = "export/fr-vs-hb-" + it_day_range[il-1].strftime('%m%d') + '.png'
 
plt.savefig(ofname, dpi=120)
#plt.show()
