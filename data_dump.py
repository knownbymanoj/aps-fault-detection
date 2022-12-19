import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://manojnag:manoj%40123@aps-cluster-0.schwnjq.mongodb.net/test")#%40 for @ sign

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME= "aps"
COLLECTION_NAME= "sensor"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Coloumns: {df.shape}")

    #Convert Dataframe to JSON to dump records in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())#Convert df to json library
    print(json_record[0])

    #insert json records into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
