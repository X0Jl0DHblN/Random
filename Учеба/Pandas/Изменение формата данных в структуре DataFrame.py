import pandas as pd



d = [{'name':'pen', 'price':4.5, 'count':10},{'name':'book', 'price':50.2, 'count':12}]
df = pd.DataFrame(d)
print(df)
print('-'*25)
print(df.dtypes)
print('-'*25)

# Приведем тип данных в поле "count" к целым 32-х значным цифрам
# =============================================================================
# df['count'] = df['count'].astype('int32') 
# print(df.dtypes)
# print('-'*25)
# 
# =============================================================================
#  Приведем тип данных поля "count" к значениям типа данных float при помощи словаря

df['count'] = df['count'].astype({'count':'int32'}) 
print(df.dtypes)

