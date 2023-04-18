# ECE4424 Fake News Detection Project
# Topic - Dataset cleaning
# Authors - Luc Phan, Kevin Lizarazu
# Last Modified: 04/17/23

import pandas as pd
# import numpy as np
import string

from utils import *

class CleanText:

    def __init__(self, config_path="./config.json"):
        self.env_config = loadConfig(config_path)

    def clean(self):
        # Read CSV
        readData = pd.read_csv(self.env_config["train_path"])

        # DEBUG PRINTS
        # print("Uncleaned: ")
        # print(readdata['text'])

        # Lowercase the data
        cleanData = readData.apply(lambda x: x.astype(str).str.lower())

        # Remove punctuations
        translator = str.maketrans('', '', string.punctuation)
        cleanData['title'] = cleanData['title'].str.translate(translator)
        cleanData['text'] = cleanData['text'].str.translate(translator)

        # DEBUG PRINTS
        # print("Cleaned: ")
        # print(cleandata['text'])

        # Write to new csv file
        cleanData.to_csv("../datasets/cleanedtrain.csv")

# Testing the script here
test = CleanText()
test.clean()