#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cn = pd.read_csv('../DA/data/ncp-cn.csv',index_col='Date',parse_dates=True)
hb = pd.read_csv('../DA/data/ncp-hb.csv',index_col='Date',parse_dates=True)

ts = cn.sort_index().index[1:]
con = cn['Confirmed'].sort_index().values[1:]
con_hb = hb['Confirmed'].sort_index().values[1:]

con_xhb = con - con_hb
dcon_hb = con_hb - np.concatenate((con_hb[:-con_hb.size+1],con_hb[:-1]))
dcon_xhb = con_xhb - np.concatenate((con_xhb[:-con_xhb.size+1],con_xhb[:-1]))
plt.figure(figsize=(12,24))
plt.subplot(311)
plt.title('Total Confirmed Cases',color='#222222')
plt.plot(ts,con_hb,color='#ffb61c',marker='o',label='Hubei')
plt.plot(ts,con_xhb,color='#92c500',marker='o',label='Outside Hubei')
plt.grid()
plt.legend()
plt.gcf().autofmt_xdate()
plt.subplot(312)
plt.title('New Confirmed Cases')
plt.plot(ts,dcon_hb,'C1',marker='o',label='Hubei')
plt.plot(ts,dcon_xhb,color='#75a800',marker='o',markeredgecolor='g',label='Outside Hubei')
plt.legend()
plt.gcf().autofmt_xdate()
p = 6
plt.subplot(313)
plt.title('Growth Rate(%) of Confirmed Cases')
plt.plot(ts[p:],(100*dcon_hb/np.concatenate((con_hb[:-con_hb.size+1],con_hb[:-1])))[p:],color='#f83a3a',marker='o',label='Hubei')
plt.plot(ts[p:],(100*dcon_xhb/np.concatenate((np.array([0.1,0.1,0.1,0.1,0.1,7]),con_xhb[5:-1])))[p:],color='#669900',marker='o',label='Outside Hubei')
plt.ylabel('%',{'fontsize':14})
plt.legend()
plt.grid()
plt.gcf().autofmt_xdate()
plt.show()
