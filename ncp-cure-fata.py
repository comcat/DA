#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

p=9

cn = pd.read_csv('data/ncp-cn.csv',index_col='Date',parse_dates=True)
hb = pd.read_csv('data/ncp-hb.csv',index_col='Date',parse_dates=True)
ts = cn.sort_index().index[1:]

con = cn['Confirmed'].sort_index().values[1:]
con_hb = hb['Confirmed'].sort_index().values[1:]

rec = cn['Recovered'].sort_index().values[1:]
rec_hb = hb['Recovered'].sort_index().values[1:]

dea = cn['Deaths'].sort_index().values[1:]
dea_hb = hb['Deaths'].sort_index().values[1:]

plt.figure(figsize=(12,28))

plt.subplot(211)
plt.title('Cure Rate (%)')
plt.plot(ts[p:], ((rec-rec_hb)/(con-con_hb)*100)[p:], 'C2', label='Outside Hubei',marker='o')
plt.plot(ts[p:], (rec_hb/con_hb*100)[p:], 'C9', label='Hubei',marker='o')
plt.ylabel('%',{'fontsize':14})
plt.grid()
plt.legend()

plt.subplot(212)
plt.title('Fatality Rate (%)')
plt.plot(ts[p:], ((dea-dea_hb)/(con-con_hb)*100)[p:], 'C1', label='Outside Hubei',marker='o')
plt.plot(ts[p:], (dea_hb/con_hb*100)[p:], 'C8', label='Hubei',marker='o')
plt.ylabel('%',{'fontsize':14})
plt.grid()
plt.legend()

plt.gcf().autofmt_xdate()
plt.show()
