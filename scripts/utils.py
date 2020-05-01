import pandas as pd

def save_ch_neighbours(filename='ourworldindatadeathetc.csv'):
    df = pd.read_csv(filename)
    df.loc[df['location'] == 'Switzerland'].to_csv('switzerland.csv')
    df.loc[df['location'] == 'France'].to_csv('france.csv')
    df.loc[df['location'] == 'Italy'].to_csv('italy.csv')
    df.loc[df['location'] == 'Germany'].to_csv('germany.csv')
    df.loc[df['location'] == 'Austria'].to_csv('austria.csv')
    df.loc[df['location'] == 'Liechtenstein'].to_csv('liechtenstein.csv')

def load_ch_neighbours():
    return pd.read_csv('switzerland.csv'), pd.read_csv('france.csv'),\
           pd.read_csv('italy.csv'), pd.read_csv('germany.csv'),\
           pd.read_csv('austria.csv'), pd.read_csv('liechtenstein.csv')

def drop_prepandemic_dates(data):
    prepandemic_dates = []
    for index, row in data.iterrows():
        prepandemic_dates.append((index))
        if row['new_cases'] > 0:
            break
    return data.drop(labels=prepandemic_dates)
