import pandas as pd



s = pd.Series([1, 2, 3, 4],['a', 'b', 'c', 'd'])
print(s)

d = {'A':[1,2,3], 'B':[10,20,30], 'C':[15,25,35]}
df = pd.DataFrame(d, index = ['a', 'b', 'c'])
print(df)

print('\nВыбор случайного элемента структуры Series с помощью метода "sample()":')
print(s.sample())

print('\nВыбор нескольких случайных элементов из структуры Series с помощью метода "sample()":')
print(s.sample(3)) 

print('\nВыбор случайного столбца структуры DF с помощью метода "sample()":')
print(df.sample(axis = 1))

print('\nВыбор нескольких случайных столбцов структуры DF с помощью метода "sample()":')
print(df.sample(n = 2, axis = 1))

print('\nВыбор случайной строки из структуры DF с помощью метода "sample()":')
print(df.sample())  # при этом ось не указывается     

print('\nВыбор нескольких случайных строк из структуры DF с помощью метода "sample()":')
print(df.sample(n = 2)) # при этом ось не указывается

     