#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

p = pd.read_csv('../data/da01-press.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))
p = p.drop(columns=['name'])

d = p['Press'].values
l = p.index

meanv = np.array([np.mean(d)]*len(d))
trimmeanv = np.array([stats.trim_mean(d, 0.2)]*len(d))
medianv = np.array([np.median(d)]*len(d))

plt.figure(figsize=(12,9))
plt.plot(l, d, marker='.',linewidth=0.8,color='C1')

plt.plot(l, meanv, '-r', linewidth=1, alpha=0.8, label='Mean='+format(np.mean(d),".2f"))

plt.plot(l, trimmeanv, '-C9', linewidth=1, alpha=1, label='Trim mean='+format(stats.trim_mean(d,0.2),".2f"))

plt.plot(l, medianv, '-C2', linewidth=0.9, label='Meidan='+format(np.median(d),".2f"))

plt.legend()
plt.grid(linewidth=0.5)
plt.show()
