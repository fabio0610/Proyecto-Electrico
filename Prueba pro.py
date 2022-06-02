import pandas as pd
from openpyxl import load_workbook
# dataframe Name and Age columns
df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                   'Age': [10, 0, 30, 50]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel('demo.xlsx')
texto= df.at[2,'Name']
print(texto)
df.at[2,'mampichas']='Abdul'
df.to_excel('demo2.xlsx')
# Close the Pandas Excel writer and output the Excel file.
#writer.save()