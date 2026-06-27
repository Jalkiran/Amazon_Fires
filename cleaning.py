import pandas as pd
df=pd.read_csv(r"C:\Users\Acer\Downloads\amazon_fires.csv",encoding='latin1')

#Average of fires of each state
print(df["numero"].dtype)