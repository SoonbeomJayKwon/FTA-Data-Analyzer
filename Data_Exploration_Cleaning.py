import pandas as pd

file_path = 'C:/Users/soonb/OneDrive/바탕 화면/Documents/programming/Python/FTA-Data-Analyzer/countryFiles_South_Korea.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# duplicates = df[df.duplicated(['Hs Code '])]
# print(duplicates)

# print(df.columns)

# print(df.head())
# print(df.describe())

# nine_digit_rows = df[df['Hs Code '].astype(str).str.match(r'^\d{9}$')]
# duplicate_nine_digit_rows = nine_digit_rows[nine_digit_rows.duplicated(subset=['Hs Code '], keep=False)]


# print(duplicate_nine_digit_rows)

# print(df.info)