import os
import pandas as pd

from src.logger import get_logger
from src.custom_exception import CustomException

import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError ("File is not found at given path")

        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the yaml config file")

            return config
    except Exception as e:
        logger.error("Error while reading yaml file")
        raise CustomException("Filed to read yaml file", e)
        

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error("Error while loading data")
        raise CustomException("Filed to load data", e)
        
