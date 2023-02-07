import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db_url = "sqlite:///bdd_olist.sqlite"
engine = create_engine(db_url)

if not database_exists(engine.url):
    create_database(engine.url)

con = engine.connect()

csv_files_name = os.listdir("data")

for csv in csv_files_name:
    df = pd.read_csv("data/"+csv)
    df.to_sql(csv.replace(".csv",""), con = engine,if_exists = "replace",index=False)