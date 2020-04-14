#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

plt.rcParams['legend.fontsize'] = 'x-large'
plt.rcParams['ytick.labelsize'] = 13
 
it = pd.read_csv("./data/covid-19-who/Italy.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

sp = pd.read_csv("./data/covid-19-who/Spain.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

ge = pd.read_csv("./data/covid-19-who/Germany.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

fr = pd.read_csv("./data/covid-19-who/France.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

uk = pd.read_csv("./data/covid-19-who/uk.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

us = pd.read_csv("./data/us.csv", skipinitialspace=True, index_col='Date', parse_dates=True)

usc = us['Confirmed'][-1]
itc = it['Confirmed'][0]
spc = sp['Confirmed'][0]
gec = ge['Confirmed'][0]
frc = fr['Confirmed'][0]
ukc = uk['Confirmed'][0]

usd = us['Deaths'][-1]
itd = it['Deaths'][0]
spd = sp['Deaths'][0]
ged = ge['Deaths'][0]
frd = fr['Deaths'][0]
ukd = uk['Deaths'][0]

print("it: ", itd/itc*100, "%")
print("sp: ", spd/spc*100, "%")
print("ge: ", ged/gec*100, "%")
print("fr: ", frd/frc*100, "%")
print("uk: ", ukd/ukc*100, "%")
print("us: ", usd/usc*100, "%")

usc = us['Confirmed']
itc = it['Confirmed']
spc = sp['Confirmed']
gec = ge['Confirmed']
frc = fr['Confirmed']
ukc = uk['Confirmed']

usd = us['Deaths']
itd = it['Deaths']
spd = sp['Deaths']
ged = ge['Deaths']
frd = fr['Deaths']
ukd = uk['Deaths']

us_ts = us.index

plt.figure(figsize=(14.4,21.6))

plt.title('Crude Case Fatality Ratio (%)\n', {'fontsize':17, 'fontweight':'bold','color': '#0b0c0c', 'verticalalignment':'top'})

plt.plot(usd/usc*100, 'C1', label='United States',marker='o')

plt.ylabel('%',{'fontsize':14})
plt.grid(linewidth=0.6,alpha=0.6)
plt.legend()

plt.gcf().autofmt_xdate()

#plt.show()

# rect(left,bottom,right,top)
plt.tight_layout(pad=1.6, rect=(0.02,0.01,0.95,0.96))
ofname = "export/us-fata-" + us_ts[-1].strftime('%m%d') + '.png'
plt.savefig(ofname, dpi=120)
