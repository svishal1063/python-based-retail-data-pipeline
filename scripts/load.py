import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:<db_password>@localhost:5432/retail_db"

def load_data(df):

    try:

        engine = create_engine(DB_URI)
        ## Read the ingested data


        ## Load the data into PostGreSQL
        df.to_sql("sales",engine,if_exists = "append",index=False)
        print("Loading successful")


    except Exception as e:
        print("Something went wrong")
        print(e)





    




