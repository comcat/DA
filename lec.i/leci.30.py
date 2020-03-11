#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t1 = pd.read_csv('../data/da02-temp-0948.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t2 = pd.read_csv('../data/da02-temp-0019.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

t3 = pd.read_csv('../data/da02-temp-1144.csv', index_col='time', date_parser=lambda x: pd.to_datetime(float(x)+28800000000000))

plt.plot(t1.index, t1['Temp'], label='t1')
plt.plot(t2.index, t2['Temp'], label='t2')
plt.plot(t3.index, t3['Temp'], label='t3')

plt.legend()
plt.show()
