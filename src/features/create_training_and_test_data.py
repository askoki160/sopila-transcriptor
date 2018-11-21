import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

from settings import TRAINING_DIR, TEST_DIR, FILTER_SPECTROGRAM_DIR
from helpers.file_helpers import create_directory, clear_dir
from os import listdir, remove
from shutil import copy2
from random import shuffle

clear_dir(TRAINING_DIR)
clear_dir(TEST_DIR)

folders = listdir(FILTER_SPECTROGRAM_DIR)
folders.sort()

training_volume = 0.8

for folder in folders:
    create_directory(TRAINING_DIR + folder + '/')
    create_directory(TEST_DIR + folder + '/')

    folder_files = listdir(FILTER_SPECTROGRAM_DIR + folder + '/')
    # randomize data
    for i in range(100):
        shuffle(folder_files)

    split_index = int(training_volume * len(folder_files))

    training_files = folder_files[:split_index]
    for filename in training_files:
        copy2(FILTER_SPECTROGRAM_DIR + folder + '/' + filename, TRAINING_DIR + folder + '/' + filename)

    test_files = folder_files[split_index:]
    for filename in test_files:
        copy2(FILTER_SPECTROGRAM_DIR + folder + '/' + filename, TEST_DIR + folder + '/' + filename)
