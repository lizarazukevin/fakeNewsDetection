# ECE4424 Fake News Detection Project
# Topic - Dataset cleaning
# Authors - Luc Phan, Kevin Lizarazu
# Last Modified: 04/17/23

import pandas as pd
import nlkt
# import numpy as np
import string
import re

from gensim.models import Word2Vec
from nltk.corpus import stopwords
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


# preprocessing // Ref: https://www.youtube.com/watch?v=Otde6VGvhWM&ab_channel=KrishNaik
# paragraph = "bruh1"
# text = re.sub(r'\[[0-9]*\]', ' ', paragraph)
# text = re.sub(r'\s+', ' ', text)
# text = text.lower()
# text = re.sub(r'\d', '', text)
# text = re.sub (r'\s+', '', text)

# sentences = nltk.sent_tokenize(text)
# sentences = [nltk.work_tokenize(sentence) for sentence in sentences]

# for i in range(len(sentences)):
#   sentences[i] = [word for word in sentences[i] if not in stopwords.words('english')]

# model = Word2Vec(sentences, min_count=1)
# words = model.wv.vocab

# similar = model.wv.most_similar('Something')