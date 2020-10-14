import pandas as pd

# Read File
sample1 = pd.read_excel("sample.xlsx", sheet_name="Sheet1")
print(sample1)

sample2 = pd.read_excel("sample.xlsx", sheet_name="Sheet2")
print(sample2)