#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

p = pd.read_csv('./data/da03-press.csv',index_col='time')
pp = p['Press']

pp.plot.hist(bins=200, rwidth=.9, density=True, color='C2', alpha=0.8)

pp.plot.kde(bw_method=0.1737, color='C1')

plt.ylabel('Probability'); plt.xlim(xmin=3200,xmax=4200); plt.xlabel('hPa')
plt.grid(linewidth=0.8)
plt.show()
 
#sns.distplot(pp)
#plt.show()
