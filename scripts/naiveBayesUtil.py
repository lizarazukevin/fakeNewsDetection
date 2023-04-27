# ECE4424 Fake News Detection Project
# Topic - Naive Bayes
# Authors - Kevin Lizarazu
# Last Modified: 04/17/23

import numpy as np

from utils import *
# need to put the text extraction as part of the utils
from collections import defaultdict

class NaiveBayesPredictor:

    def __init__(self, config_path="./config.json"):
        self.env_config = loadConfig(config_path)
        self.model = defaultdict()
        # self.word_probs = defaultdict(list)
        # self.class_probs = defaultdict(list)
        self.raw_train

        print(self.env_config)
    
    # here we would either need to read the path to the clean data or in data extraction have it ready for us
    def train(self, params=None,):


        # self.labels = np.unique(train_labels)

        # d, n = train_data.shape
        # num_classes = self.labels.size

        # for c in range(num_classes):
        #     print c