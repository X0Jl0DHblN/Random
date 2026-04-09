import pandas as pd
from io import StringIO

data = 'A,B,C\n1,3,\n5,10,15\n7,25,'
df = pd.read_csv(StringIO(data))
print("Исходный DataFrame:")
print(df)
print()
print('Добавим строку к нашему DataFrame')
print('=' * 30)
df.loc[3] = {'A':16, 'B':None, 'C':13.25} 
#df.loc[len(df)] = {'A': 16, 'B': None, 'C': 13.25} 
#или
#df.loc[3] = [16, None, 13.25]
print(df)
print()
print('Заменим "пустые" значения на 0')
print('=' * 30)
print(df.fillna(0))
print()
print('Заменим нулевые значения на среднюю')
print('=' * 30)
print(df.fillna(df.mean()))
print()
print('Вывод')
print('=' * 30)
print(pd.isnull(df))
print(df.info())

