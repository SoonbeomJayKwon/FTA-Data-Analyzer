import pandas as pd

file_path = 'C:/Users/soonb/OneDrive/바탕 화면/Documents/programming/Python/FTA-Data-Analyzer/countryFiles_South_Korea.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# print(df.head())
print(df.describe())
