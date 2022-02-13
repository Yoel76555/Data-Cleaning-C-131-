import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)

del df["Star_name"] 
del df["Distance"] 
del df["Radius"] 
del df["Mass"] 
del df["Luminosity"] 

df.to_csv('main.csv')