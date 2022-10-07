#### Imports ####

from sqlalchemy import create_engine

import pandas as pd 




#### Create Connection To VM Env ####

MYSQL_HOSTNAME = '20.100.177.191' ## we'll put the ip address of the Azure vm we spun up for this repo

MYSQL_USER = 'zhou'

MYSQL_PASSWORD = 'ahi2022'

MYSQL_DATABASE = 'isaac'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
connection_string 

db = create_engine(connection_string)
db

query = 'select * from isaac.table1;'
query

df = pd.read_sql(query, con=db)

real_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/descriptive/example1/data/data.csv')
real_df

real_df.to_sql('fake_table', con=db, if_exists='replace')