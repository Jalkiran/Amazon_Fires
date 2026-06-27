import pandas as pd
df=pd.read_csv(r"C:\Users\Acer\Downloads\amazon_fires.csv",encoding='latin1')

#Average of fires of each state
print(df["numero"].dtype)

df["numero"] = df["numero"].str.replace(".", "", regex=False)
df["numero"] = pd.to_numeric(df["numero"], errors='coerce')
print(df["numero"].dtype)

print(df.groupby("estado")["numero"].mean())

#Cleaning the data
print(df.isnull().sum())

df_dropped = df.dropna()
print(len(df_dropped))