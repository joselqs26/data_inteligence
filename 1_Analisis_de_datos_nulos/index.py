import pandas as pd

df1 = pd.read_csv('All_Data_Aldi.csv')
print( df1.shape )
print( df1.isnull().sum() )