#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p = pd.read_csv('../data/da03-temp-0019.csv',index_col='time')
pp = p['Temp']  # pp is pd.Series

pp.plot.hist(bins=48, rwidth=.9, density=True, color='C0', alpha=0.8, label='0019')

pp.plot.kde(bw_method=0.6, color='C1', alpha=0.7, label='KDE')

plt.ylabel('Probability'); plt.xlabel(u'°C')

#plt.xlim(xmin=-30, xmax=30)

medy = np.linspace(0, 0.035, 100)
medx = np.repeat(pp.median(), medy.size)
plt.plot(medx, medy, color='r', alpha=0.5, label='median ='+str(pp.median()))

plt.legend()
plt.grid(linewidth=0.8)
plt.show()
