#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

p = pd.read_csv('./data/da01-press.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))
p = p.drop(columns=['name'])

d = p['Press'].values
l = p.index

mean = np.mean(d)
trimmean = stats.trim_mean(d,0.2)
median = np.median(d)

meanv = np.array([np.mean(d)]*len(d))
trimmeanv = np.array([stats.trim_mean(d, 0.2)]*len(d))
medianv = np.array([np.median(d)]*len(d))

stdv = np.array([np.std(d)]*len(d))
iqrv = np.array([stats.iqr(d)]*len(d))
madv = np.array([stats.median_absolute_deviation(d)]*len(d))

print("std =", format(np.std(d),".2f"), " iqr =", format(stats.iqr(d),".2f"), " mad =", format(stats.median_absolute_deviation(d),".2f"))

mean_up = meanv + stdv
mean_down = meanv - stdv

median_up = medianv + iqrv
median_down = medianv -iqrv

mad_up = trimmeanv + madv
mad_down = trimmeanv - madv

#plt.figure(figsize=(10,7))

#plt.plot(l, meanv, '-C1', linewidth=1, alpha=0.6, label='Mean='+format(np.mean(d),".2f"))
#plt.plot(l, mean_up, '-.C1', alpha=0.6, linewidth=1)
#plt.plot(l, mean_down, '-.C1', alpha=0.6, linewidth=1)

#plt.plot(l, trimmeanv, '-C9', linewidth=1, alpha=0.7, label='Trim mean='+format(stats.trim_mean(d,0.2),".2f"))
#plt.plot(l, mad_up, ':C9', alpha=0.9, linewidth=1)
#plt.plot(l, mad_down, ':C9', alpha=0.7, linewidth=1)

#plt.plot(l, medianv, '-C2', linewidth=1, label='Meidan='+format(np.median(d),".2f"))
#plt.plot(l, median_up, ':C2', linewidth=1)
#plt.plot(l, median_down, ':C2', linewidth=1)

p.plot(kind='hist',bins=60, color='C1')

#l = np.array([mean]*len(d))
#plt.plot(l, meanv)

plt.legend()
plt.grid(linewidth=0.5)
plt.show()
