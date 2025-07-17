import pyodbc
import pandas

db = pyodbc.connect('Driver={SQL Server};'
                    'Server=SQL.Samorodov.SU;'
                    'Database=R;'
                    'UID=Data Science;'
                    'PWD=Pa$$w0rd')

SQL_Query = pandas.read_sql_query ('''select * from mtcars;''', db)

dfCars = pandas.DataFrame (SQL_Query)

print (dfCars)