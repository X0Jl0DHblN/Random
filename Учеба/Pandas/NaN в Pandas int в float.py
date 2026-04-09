import pandas as pd
import numpy as np

s = pd.Series([1,2,3])
print(s)
print(s.dtype)
print()
s[1] = np.nan
print(s)
print(s.dtype)
