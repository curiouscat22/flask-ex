import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('countries.csv')
df.dropna()
df.rename(columns = {'Alpha2_code':'alpha2', 'Alpha3_code':'alpha3', 'Numeric_code':'nuCode'}, inplace = True)

engine = create_engine('postgresql+psycopg2://postgres:Testing123@localhost:5432/test')

df.to_sql('counties', engine,index=False, if_exists='replace')