# ECE4424 Fake News Detection Project
# Topic - Utils
# Authors - Kevin Lizarazu, Luc Phan
# Last Modified: 05/04/23

import json
import csv
import nltk
import pandas as pd
import numpy as np
import string
import chardet

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from pandas import *


# Loads configuration contents of JSON structure 
def loadConfig(path: str) -> dict:

    cfg = json.load(open(path, "r"))
    for key, element in cfg.items():
        if isinstance(element, list):
            cfg[key] = np.array(element)
            
    return cfg


# Loads the data from a data path and returns as a DataFrame
def loadData(file_path: str) -> DataFrame:

    # Stores the contents of csv in a DataFrame
    read_data = pd.read_csv(file_path)

    return read_data

# Cleans the data using various techniques such as lowercasing, alpha check, and lemmatization
def cleanData_1(data: DataFrame) -> DataFrame:
    
    # Lowercase the data
    cleandata = data.apply(lambda x: x.astype(str).str.lower())

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleandata['title'] = cleandata['title'].str.translate(translator)
    cleandata['text'] = cleandata['text'].str.translate(translator)

    # Returns the DataFrame with text that has been lowered and rid of punctutation
    return cleandata


# Cleans the data further by implementing filters for stop words and lamination
def cleanData_2(data_f: DataFrame) -> DataFrame:
    stop_words = set(stopwords.words('english'))
    data_f['text'] = data_f['text'].apply(lambda x: [word for word in nltk.word_tokenize(x.lower()) if word.isalpha() and word not in stop_words])

    lemmatizer = WordNetLemmatizer()
    data_f['text'] = data_f['text'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

    return data_f

# Attempt at making a class for Naive 
class NaiveBayesPredictor:

    def __init__(self, config_path="./config.json"):
        self.env_config = loadConfig(config_path)
        self.model = defaultdict()
        # self.word_probs = defaultdict(list)
        # self.class_probs = defaultdict(list)
        # self.raw_train

        print(self.env_config)
    
    # here we would either need to read the path to the clean data or in data extraction have it ready for us
    def train(self, params=None,):
        print("Training!")

##############################################################
# Testing
##############################################################

# # Loads the data from a data path and returns as a dict
# def loadData(file_path: str) -> dict:

#     # dictionary structure to hold sentence id and contents
#     # specific to this project --> {id: {'title', 'text', 'subject', 'date', 'label'}}
#     data_dict = dict()

#     with open(file_path, 'rb') as f:
#         res = chardet.detect(f.read())

#     # opens the csv file in read mode and saves entries to dict
#     with open(file_path, newline='', encoding=res['encoding']) as f:

#         # reads the file here and delimits cells based on tabs
#         r = csv.reader(f, delimiter='\t')

#         for id, line in enumerate(r):

#             # first row that saves features as column headers
#             if id == 0:
#                 features = [x for x in line]
#                 continue
            
#             # assigns contents of each row to each feature in the dictionary
#             data_dict[id] = { feat:line[f_id] for f_id, feat in enumerate(features) }

#     print(data_dict[1])

#     json_obj = json.dumps(data_dict, indent=4)
#     with open("sample_out.json", "w") as outfile:
#         outfile.write(json_obj)

#     return data_dict


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