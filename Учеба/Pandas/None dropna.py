import pandas as pd
import numpy as np

s1 = pd.Series([1,None,3])
print(s1)
print(s1.dtype)
print(s1.dropna())