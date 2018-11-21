# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

from google_drive_downloader import GoogleDriveDownloader as gdd
from helpers.file_helpers import clear_dir, create_directories
from settings import RAW_DATA_DIR, INTERIM_DATA_DIR, \
    PROCESSED_DATA_DIR, SPECTROGRAM_PATH, FILTER_DIR, \
    FILTER_SPECTROGRAM_DIR, CUT_DIR, TRAINING_DIR, TEST_DIR


# create base data folder structure
directories_to_create = [
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    SPECTROGRAM_PATH,
    FILTER_DIR,
    FILTER_SPECTROGRAM_DIR,
    CUT_DIR,
    TRAINING_DIR,
    TEST_DIR
]

# create directories in data folder
create_directories(directories_to_create)

# delete contents of raw folder
clear_dir(RAW_DATA_DIR)


FILE_ID = '1jMiQ4iMKaUgN3EDFPS5sSFfRDCH-5Bne'
gdd.download_file_from_google_drive(
    file_id=FILE_ID,
    dest_path=RAW_DATA_DIR + 'data.zip',
    unzip=True
)

print("Removing downloaded zip file ...")
os.remove(RAW_DATA_DIR + 'data.zip')
