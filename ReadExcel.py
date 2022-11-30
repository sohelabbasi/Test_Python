import pandas as pd
Excel_File = "C:\\Users\\13479\\Desktop\\Marketing Data.xlsx"
df1 = pd.read_excel(Excel_File, sheet_name='Participants')
print(df1)
print(df1['LastName'])
print(df1['FirstName'])
df2 = pd.read_excel(Excel_File, sheet_name='Vendors')
print(df2['Company'])
print(df2['City'])