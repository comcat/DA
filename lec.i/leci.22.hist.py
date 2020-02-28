#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

p = pd.read_csv('../data/da01-press.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))
p = p.drop(columns=['name'])

d = np.random.normal(19, 0.5, len(p.index))
l = p.index

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

plt.hist(d, bins=60, color='C1')

plt.legend()
plt.grid(linewidth=0.5)
plt.show()
