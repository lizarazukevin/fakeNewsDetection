# ECE4424 Fake News Detection Project
# Topic - Naive Bayes
# Authors - Kevin Lizarazu
# Last Modified: 04/17/23

import numpy as np

from utils import *
from collections import defaultdict

class NaiveBayesPredictor:

    def __init__(self, train_data, train_labels, config_path="./config.json"):
        self.env_config = loadConfig(config_path)
        self.labels = np.unique(train_labels)
        # self.bag = defaultdict(list)

        print(self.env_config)