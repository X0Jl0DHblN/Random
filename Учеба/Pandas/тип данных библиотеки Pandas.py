import pandas as pd
import numpy as np


d = [{'name':'pen', 'price':4.5, 'count':10},{'name':'book', 'price':50.2, 'count':12}]
df = pd.DataFrame(d)
print(df)
print()
#print(df.info())
print(df.dtypes) #так же можно использовать для получения информации DF и Series