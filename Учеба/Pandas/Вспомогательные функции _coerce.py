import pandas as pd

df = pd.read_csv('E:/pogoda.csv', sep = ',')
print(df)
print(df.dtypes)

df['Температура'] = pd.to_numeric(df['Температура'], errors = 'coerce')
df['Давление'] = pd.to_numeric(df['Давление'], errors = 'coerce')
df['Дата'] = pd.to_numeric(df['Дата'], errors = 'coerce')
print(df)
print(df.dtypes)

print(df)