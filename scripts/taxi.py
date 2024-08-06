import pandas as pd
df=pd.read_csv('data/2019_Yellow_Taxi_Trip_Data.csv')
print(df.head(5))
print(df.shape)
print(df.vendorid)
print(df[['vendorid','total_amount']])
print(df[1:4])