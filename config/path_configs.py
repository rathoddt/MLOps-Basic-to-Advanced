import os

# ---------- Data Ingestion ------------

RAW_DIR = "artifacts/raw"
RAW_FILE_PATH= os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH = "config/config.yaml"

#--------- Data Processing --------------
PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAINED_PATH = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_PATH = os.path.join(PROCESSED_DIR, "processed_test.csv")