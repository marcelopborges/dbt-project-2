import os
import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass


base = os.getcwd()
path_tables = os.path.join(base, 'tables')
tables = os.listdir(path_tables)
user = input('Database user: ')
password = getpass('Database password: ')

con = create_engine(f'postgresql+psycopg2://{user}:{password}@localhost:5432/postgres')

for table in tables:
    path_table = os.path.join(path_tables, table)
    table = table.replace('.csv', '')
    df = pd.read_csv(path_table)
    df.to_sql( 
        table, 
        con, 
        schema='transacional',
        if_exists='replace', 
        index=False
    )
    print(f'Table {table} imported successfully')   