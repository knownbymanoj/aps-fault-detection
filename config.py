import pymongo
import pandas as pd
import json
import os
from dataclasses import dataclass
# Provide the mongodb localhost to connect python to mongodb

@dataclass
class EnvironmentVariable():
    mongodb_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongodb_url)

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME= "aps"
COLLECTION_NAME= "sensor"