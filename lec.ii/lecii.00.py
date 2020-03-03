#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

p = pd.read_csv('../data/da03-press.csv',index_col='time')
pp = p['Press']  # pp is pd.Series

pp.plot.hist(bins=150, rwidth=.9, color='C1', alpha=0.8)

plt.ylabel('Counts'); plt.xlabel('hPa')
plt.xlim(xmin=3200,xmax=4200)
plt.grid(linewidth=0.8)
plt.show()
