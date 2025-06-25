import os
import pandas as pd 
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException

from config.path_configs import *

from utils.common_fuctions import read_yaml 

logger = get_logger(__name__)

class DataIngestion: 
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ration = self.config["train_ration"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data ingestion started with {self.bucket_name} and file is {self.file_name}")
    
    def download_csv_from_gcp(self ):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            
            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"CSV file is successfulky downloaded to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error("Error while reading CSV file")
            raise CustomException("Failed to laod CSV file", e)

    def train_test_split(self):
        try:    
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)
            train_set, test_set = train_test_split(data, test_size=1-self.train_test_ration, random_state=42)
            train_set.to_csv(TRAIN_FILE_PATH, index=False)
            test_set.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Trained data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into train and test sets", e)
    
    def run(self):
        try:
            self.download_csv_from_gcp()
            self.train_test_split()
            logger.info("Data ingestion completed")
        except CustomException as ce:
            logger.error( f"CustomException: {ce}")
        finally:
            logger.info("Data ingestion completed")


if __name__ == "__main__":
    data_ingestion=DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()


        