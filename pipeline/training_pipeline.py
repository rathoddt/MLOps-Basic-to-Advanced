from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
# from utils.common_functions import read_yaml
# from utils.common_fuctions import read_yaml 
# from utils.common_functions import read_yaml
from utils.common_functions import read_yaml 
from src.logger import get_logger
from config.paths_config import *

import sys 
logger = get_logger(__name__)

if __name__=="__main__":
    logger.info(f"-------------------------------------------------")
    ### 1. Data Ingestion

    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ### 2. Data Processing

    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ### 3. Model Training

    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()