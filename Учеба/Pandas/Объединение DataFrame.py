import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A':['a1','a2','a3'],
                    'B':['b1','b2','b3'],
                    'C':['c1','c2','c3']}, index = [0,1,2])

df2 = pd.DataFrame({'A':['a4','a5','a6'],
                    'B':['b4','b5','b6'],
                    'C':['c4','c5','c6']}, index = [3,4,5])

df4 = pd.DataFrame({'D':['d1','d2','d3'],
                    'E':['e1','e2','e3']})

df5 = pd.DataFrame({'F':['f1','f2','f3'],
                    'G':['g1','g2','g3']}, index = [3,4,5])

dfx = pd.DataFrame({'D':['d2','d3','d4'],
                    'E':['e2','e3','e4']}, index = [1,2,3])


df3 = pd.concat([df1,df2])
print(df3)
print('*'*30)
df4 = pd.concat([df1,df4],axis = 1)
print(df4)
print('*'*30)
df6 = pd.concat([df1,df5],axis = 1)
print(df6)
print('*'*30)
df7 = pd.concat([df1,df2], keys = ['df1','df2'])
print(df7)
print(df7.loc['df2'])
print('*'*30)
df8 = pd.concat([df1,dfx],axis = 1, join = 'auter')
print(df8)