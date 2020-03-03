#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p = pd.read_csv('../data/da03-temp-1144.csv',index_col='time')
pp = p['Temp']  # pp is pd.Series

pp.plot.hist(bins=9, rwidth=.9, color='C2', alpha=0.8, label='1144')

plt.ylabel('Counts'); plt.xlabel(u'°C')

plt.xlim(xmin=4, xmax=18)

medy = np.linspace(0, 80, 100)
medx = np.repeat(pp.median(), medy.size)
plt.plot(medx, medy, color='r', alpha=0.3, label='median ='+str(pp.median()))

plt.legend()
plt.grid(linewidth=0.8)
plt.show()
