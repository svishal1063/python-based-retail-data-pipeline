from ingest import ingest_data
from transform import transform_data
from load import load_data


def run_pipeline():
    
    try:
        df = ingest_data()
    except Exception as e:
        print("An error has occured in the ingestion")
        print(e)

    try:
        df = transform_data(df)
    except Exception as e:
        print("An error has occured in the transformation")
        print(e)

    
    try:
        df = load_data(df)
    except Exception as e:
        print("An error has occured while loading the data into the database")
        print(e)


    print("Pipeline has executed successfully")


if __name__ == "__main__":
    run_pipeline()
