#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

d = np.array([3, 1, 5, 3, 15, 6, 7, 2])

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

mad_up = medianv + madv
mad_down = medianv - madv

plt.plot(d,'o',color='C1')

plt.plot(meanv, '-C1', alpha=0.6, label='Mean='+format(np.mean(d),".2f"))
plt.plot(mean_up, ':C1', alpha=0.6)
plt.plot(mean_down, ':C1', alpha=0.6)

plt.plot(trimmeanv, '-C8', alpha=0.7, label='Trim mean='+format(stats.trim_mean(d,0.2),".2f"))
plt.plot(mad_up, ':C8', alpha=0.7)
plt.plot(mad_down, ':C8', alpha=0.6)

plt.plot(medianv, '-C2', label='Meidan='+format(np.median(d),".2f"))
plt.plot(median_up, ':C2')
plt.plot(median_down, ':C2')

plt.legend()
plt.grid()
plt.show()
