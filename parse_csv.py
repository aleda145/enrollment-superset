import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:a_strong_postgrespassword@localhost:5433/superset')

years = range(1995,2022)
big_df = pd.DataFrame()
for year in years:
    print(f"Reading year: {year}")
    df = pd.read_csv(f'./enrollment_statistics/HT{year}.csv', sep = ";")
    df = df.dropna()
    df = df[df.Kön != "Total"]
    df = df[df.Åldersgrupp != "Total"]
    df['year'] = pd.Timestamp(f"{year}-09-01")
    big_df = big_df.append(df)
big_df.columns = ['semester', 'school', 'program', 'gender', 'age', 'number', 'year']
print(big_df)
big_df.to_sql(
    'enrollment',
    con=engine,
    index=False,
    if_exists='replace'
)


