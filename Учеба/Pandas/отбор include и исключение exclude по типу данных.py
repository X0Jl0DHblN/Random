import pandas as pd

df = pd.read_csv('E:/pogoda.csv', sep = ',')
print(df)
print(df.dtypes)

print('\nКонвертируем значения ')
convert_temperature = lambda t: t.replace('°C','').strip()
convert_pressure = lambda p: p.replace('мм.р.с.','').strip()
convert_osadki = lambda b: True if b == 'Да' else False

df['Температура'] = df['Температура'].apply(convert_temperature).astype('float64')
df['Давление'] = df['Давление'].apply(convert_pressure).astype('int64')
df['Осадки'] = df['Осадки'].apply(convert_osadki).astype('bool')
df['Дата'] = pd.to_datetime(df['Дата'], format= '%d.%m.%Y')
print(df.dtypes)

# =============================================================================
# print(df.select_dtypes(include=['float64','int64']))
# =============================================================================
print(df.select_dtypes(exclude='datetime'))