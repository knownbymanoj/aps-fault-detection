# import pymongo

# # Provide the mongodb localhost url to connect python to mongodb.
# client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# # Database Name
# dataBase = client["neurolabDB"]

# # Collection  Name
# collection = dataBase['Products']

# # Sample data
# d = {'companyName': 'iNeuron',
#      'product': 'Affordable AI',
#      'courseOffered': 'Machine Learning with Deployment'}

# # Insert above records in the collection
# rec = collection.insert_one(d)

# # Lets Verify all the record at once present in the record with all the fields
# all_record = collection.find()

# # Printing all records present in the collection
# for idx, record in enumerate(all_record):
#      print(f"{idx}: {record}")


# from sensor.logger import logging
# from sensor.exception import SensorException
# import sys,os

# def test_logger_and_exception():
#      try:
#           logging.info("Starting the test_logger_and_exception")
#           result = 3/0       
#           print(result)
#           logging.info("Stopping the test_logger_and_exception")
          
#      except Exception as  e:
#           logging.debug(str(e))
#           raise  SensorException(e, sys)

# if __name__== "__main__":

#      try:
#           test_logger_and_exception()

#      except Exception as e:
#           print(e)

# import sys,os
# from sensor.utils import get_collection_as_dataframe
# from sensor.logger import logging
# from sensor.exception import SensorException

# if __name__ == "__main__":
#     try:
#         get_collection_as_dataframe(database_name="aps", collection_name = "sensor")
    
#     except Exception as e:
#         print(e)

from sensor.entity import config_entity
import sys,os
#from sensor.utils import get_collection_as_dataframe
from sensor.logger import logging
from sensor.exception import SensorException
#from sensor.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        #get_collection_as_dataframe(database_name="aps", collection_name = "sensor")
    
    except Exception as e:
        print(e)



