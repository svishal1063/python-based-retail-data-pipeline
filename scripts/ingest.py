import pandas as pd


def ingest_data():
    
    try:
        df = pd.read_csv("/home/elijah/retail-data-pipeline/data/restaurant_sales.csv")
        print("Extraction of data is successful")
        return df
    
    except Exception as e:
        print("Something went wrong\n")
        print(e)
        return 

    