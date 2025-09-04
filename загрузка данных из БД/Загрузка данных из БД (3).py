import pyodbc
import pandas

DB = pyodbc.connect ('Driver={SQL Server};'
                     'Server=SQL.Samorodov.SU;'
                     'Database=R;'
                     'UID=Data Science;'
                     'PWD=Pa$$w0rd')

Data = pandas.read_sql_query ('''SELECT * FROM mtcars''', DB)

print (Data)
