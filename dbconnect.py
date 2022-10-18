#### Terminal Commands ####

'pip3 install python-dotenv'

'pip3 install requirements.txt'

#### Imports ####

from sqlalchemy import create_engine

import pandas as pd 

from dotenv import dotenv_values



#### Create Connection To VM Env ####

config = dotenv_values('.env') # this is where our mysql hostname, user, password, and database is stored

connection_string = f'mysql+pymysql://{config["MYSQL_USER"]}:{config["MYSQL_PASSWORD"]}@{config["MYSQL_HOSTNAME"]}/{config["MYSQL_DATABASE"]}' ## we can string together all the components to form the connection string
connection_string

db = create_engine(connection_string) ## create_engine allows us to link the database via mysql
db

query = 'select * from cybersalaries.salaries;' ## let's write a query to view information from our existing database table that we created in Azure

df = pd.read_sql(query, con=db) ## with the connection we created earlier and pandas read_sql command, we can store the query in a df and execute
df ## we see two columns, year and salary. the contents of the table are empty.
## this is expected as we have created the table with those two columns

df = pd.read_csv('Cyber_salaries.csv') ## now let's redefine df as the csv we have pulled off kaggle

df ## taking a peek at contents

df.to_sql('salaries', con=db, if_exists='replace') ## pushing the df to a table called salaries, which if exists, will be replaced. In this case it does already exist, but will be replaced with the new info we push through