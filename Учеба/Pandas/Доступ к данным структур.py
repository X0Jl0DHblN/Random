import pandas as pd
import numpy as np


s = pd.Series([1, 2, 3, 4],['a', 'b', 'c', 'd'])
print(s)
print(s['b'])
print(s[1])

d = {'A':[1,2,3], 'B':[10,20,30], 'C':[15,25,35]}
df = pd.DataFrame(d, index = ['a', 'b', 'c'])
print(df)