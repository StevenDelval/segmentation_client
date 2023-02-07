import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db_url = "sqlite:///bdd_olist.sqlite"
engine = create_engine(db_url)

con = engine.connect()

sql_queri = "SELECT * FROM olist_order_items_dataset"
df = pd.read_sql(sql=sql_queri,con=con)
print(df)