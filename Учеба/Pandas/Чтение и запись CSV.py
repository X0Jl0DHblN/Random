import pandas as pd
from io import StringIO
# =============================================================================
# csvData = """Name,Age,City
#             Bob,35,SPB
#             Vera,25,Moskva
#             Petr,40,Rostov"""
# =============================================================================
            
csvData = 'Name,Age,Sity\nBob,35,SPB\nVera,25,Moskva\nPeter,40,Rostov'
df = pd.read_csv(StringIO(csvData))
print(df)  

df.to_csv('E:/output.csv',index = ['csv_1', 'csv_2','csv_3'])         
