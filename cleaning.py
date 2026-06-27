import pandas as pd
df=pd.read_csv(r"C:\Users\Acer\Downloads\amazon_fires.csv",encoding='latin1')
print("Raw missing in numero:", df["numero"].isnull().sum())
print(df["numero"].head(20))

#Average of fires of each state
print(df["numero"].dtype)

df["numero"] = df["numero"].str.replace(" Fires", "", regex=False)
df["numero"] = df["numero"].str.replace(".", "", regex=False)
df["numero"] = pd.to_numeric(df["numero"], errors='coerce')
print(df["numero"].isnull().sum())
print(df["numero"].dtype)

print(df.groupby("estado")["numero"].mean())

#Cleaning the data
print(df.isnull().sum())

df_dropped = df.dropna()
print(len(df_dropped))

#Maintaining Data Consistency
df["estado"] = df["estado"].str.title()
print(df["estado"].unique())