import pandas as pd
from io import StringIO

data = 'A,B,C\n1,3,\n5,10,15\n7,25,'
df = pd.read_csv(StringIO(data))
print("Исходный DataFrame:")
print(df)
print()
# =============================================================================
# print('Применим к исходному DataFrame метод .dropna()')
# print('=' * 30)
# print(df.dropna())
# =============================================================================
# =============================================================================
# print('Применим к исходному DataFrame метод .dropna(axis = 1)')
# print('=' * 30)
# print(df.dropna(axis = 1))
# =============================================================================

print('Применим к исходному DataFrame метод .dropna(axis = 1, thresh = 2)')
print('=' * 30)
print(df.dropna(axis = 1, thresh = 1))
