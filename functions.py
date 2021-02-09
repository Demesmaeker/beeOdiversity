import pandas as pd
surfaces_df = pd.read_excel('data/absSurfs.xlsx', engine='openpyxl')

def qtt_pesticides(row, *args):
    total = 0
    for arg in args:
        if row[arg] > 0:
            total += row[arg]
    return total


def nb_pesticides(row, *args):
    total = 0
    for arg in args:
        if row[arg] > 0:
            total += 1
    return total


def get_surface(row):
    site = row['Site']
    classCLC = str(row['classCLC'])
    surface = surfaces_df[surfaces_df['Site'] == site][classCLC].values[0]
    return surface