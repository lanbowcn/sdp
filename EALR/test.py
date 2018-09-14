import numpy as np
import pandas as pd
import datetime
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../dataset2/jdt.csv', sep=",")
df['commitdate'] = pd.to_datetime(df['commitdate'],format='%Y/%m/%d %H:%M:%S')
df.set_index('commitdate')
print(type(df))
print(df.index)
print(type(df.index))