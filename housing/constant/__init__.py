

import os
from datetime import datetime

ROOT_DIR = os.getcwd()  #current working directory

CONFIG_DIR = "config"

CONFIG_FILE_NAME = "config_yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"(datetime.now().strftime('%Y-%m-%d:%H-%M-%s))"



## Training pipeline related variable

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'


##data injestion related variable

DATA_INJESTION_CONFIG_KEY = "data_injestion_config"
DATA_INJESTION_ARTIFACT_DIR = "data_injestion"
DATA_INJESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INJESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INJESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INJESTION_DIR_NAME_KEY= "injested_dir"
DATA_INJESTION_TRAIN_DIR_KEY= "injested_train_dir"
DATA_INJESTION_TEST_DIR_KEY = "injested_test_dir"