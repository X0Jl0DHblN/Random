import pandas as pd

S = pd.Series([1,2,3,7,3,4,2,1,1])
print(S)
print(S[S>=2]&[S<7])