import pandas as pd

df = pd.read_stata("C:/Users/jeeye/OneDrive/바탕 화면/Nederland/00_3 DSS_Semester 1_Master/0. Thesis/00. Dataset/ESJS2-microdata-2021-wave-2/CEDEFOP ESJS2 Microdata_17_03_2023_v3.dta", convert_categoricals=False)

df.head()

print(df.shape)

df['B_EMPDUR_Month'].head()
df['B_EMPDUR_Years'].head()
df['F_Pay'].head(20)

print(df['F_PAY1'].isnull().sum())

df['B_ICTWKPC'].head()
print(df['B_ICTWKPC'].isnull().sum())

df['V1115'].head()

len(df['B_NACE2'].unique())

len(df['B_ISCOD4'].unique())


colnam = df.columns[100:120]

df[0:10][colnam]
