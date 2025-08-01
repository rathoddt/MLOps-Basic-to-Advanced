import os
import pandas as pd 
from google.cloud import storage
# from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException

from config.paths_config import *

from utils.common_functions import read_yaml 
import sys 
logger = get_logger(__name__)

class DataIngestion: 
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.bucket_dir = self.config["bucket_dir"]
        self.file_names = self.config["bucket_file_names"]
        # self.train_test_ration = self.config["train_ration"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data ingestion started from bucket: {self.bucket_name} ")

    def download_csv_from_gcp(self):
        try:

            client  = storage.Client()
            bucket = client.bucket(self.bucket_name)

            logger.info("Reading files...")

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR,file_name)
                blob_path = os.path.join(self.bucket_dir, file_name)
                blob = bucket.blob(blob_path)


                if file_name=="animelist.csv":
                    # blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    data = pd.read_csv(file_path,nrows=5000000)
                    data.to_csv(file_path,index=False)
                    logger.info("Large file detected Only downloading 5M rows")
                else:
                    # blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    logger.info("Downloading Smaller Files ie anime and anime_with synopsis")
        
        # except Exception as e:
        #     logger.error("Error while downloading data from GCP")
        #     raise CustomException("Failed to download data",e)
        except Exception as e:
            logger.error(f"Error while downloading data from GCP: {str(e)}")
            raise CustomException("Failed to download data", e)        
        
    def run(self):
        try:
            logger.info("Starting Data Ingestion Process....")
            self.download_csv_from_gcp()
            logger.info("Data Ingestion Completed...")
        except CustomException as ce:
            logger.error(f"CustomException : {str(ce)}")
        finally:
            logger.info("Data Ingestion DONE...")


if __name__=="__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()        