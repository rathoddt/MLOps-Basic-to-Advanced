import os
import pandas as pd 
from google.cloud import storage
from skleatn.model_selection import train_test_split
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
        self.train_ration = self.config["train_ration"]

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
        