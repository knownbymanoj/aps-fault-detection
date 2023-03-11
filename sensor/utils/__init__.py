import panadas as pd

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    mongo_client[database_name][collection_name]