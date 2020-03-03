#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

t1 = pd.read_csv('../data/da03-temp-0948.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t2 = pd.read_csv('../data/da03-temp-0019.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t3 = pd.read_csv('../data/da03-temp-1144.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

print(t1.describe())
print(t2.describe())
print(t3.describe())

plt.plot(t1.index, t1['Temp'], label='0948')
plt.plot(t2.index, t2['Temp'], label='0019', alpha=0.8)
plt.plot(t3.index, t3['Temp'], label='1144')

plt.ylabel(u'°C')

plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(linewidth=0.5)
plt.show()
