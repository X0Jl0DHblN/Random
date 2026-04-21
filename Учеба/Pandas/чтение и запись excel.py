import pandas as pd


dfSeet1 = pd.read_excel('E:\input.xlsx',sheet_name = 'sheet1', header=None)
print(dfSeet1)
print()
# =============================================================================
# dfSheet2 = pd.read_excel('E:\input.xlsx',sheet_name = 'sheet2', header=None)
# print(dfSheet2)
# =============================================================================

with pd.ExcelFile('E:\input.xlsx') as excel:
    df1 = pd.read_excel(excel, sheet_name = 'sheet1', header=None)
print(df1)    


df1.to_excel('E:\output.xlsx', sheet_name = 'Sheet1')