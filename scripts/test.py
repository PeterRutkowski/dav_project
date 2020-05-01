import seaborn as sns
import pandas as pd

df = pd.read_csv('switzerland.csv')
print(df.keys())
for index, row in df.iterrows():
    print(row['date'], row['total_deaths'])
