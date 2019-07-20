# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from google_drive_downloader import GoogleDriveDownloader as gdd
sys.path.insert(1, os.path.join(sys.path[0], '..', '..'))
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from features.helpers.file_helpers import clear_dir, create_directories, create_directory
from settings import RAW_DATA_DIR, INTERIM_DATA_DIR, \
    PROCESSED_DATA_DIR, AMPLITUDE_ARRAY_PATH, CUT_DIR, \
    TRAINING_DIR, TEST_DIR, VALIDATION_DIR, \
    STATISTICS_DIR, ML_MODELS, FIGURES_DIR


# create base data folder structure
directories_to_create = [
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    AMPLITUDE_ARRAY_PATH,
    CUT_DIR,
    TRAINING_DIR,
    VALIDATION_DIR,
    TEST_DIR,
    FIGURES_DIR,
    STATISTICS_DIR
]

# create directories in data folder
create_directories(directories_to_create)
for directory in directories_to_create:
    for model in ML_MODELS:
        create_directory(os.path.join(directory, model['name']))

# delete contents of raw folder
clear_dir(RAW_DATA_DIR)

FILE_ID = '1SACjFsfdUZKVmBwV0bOMt9ni6B6DR6Dt'
gdd.download_file_from_google_drive(
    file_id=FILE_ID,
    dest_path=os.path.join(RAW_DATA_DIR, 'data.zip'),
    unzip=True
)

print("Removing downloaded zip file ...")
os.remove(os.path.join(RAW_DATA_DIR, 'data.zip'))


subprocess.call(
    ['python', 'merge_audio_data.py'],
    cwd="../features/"
)
