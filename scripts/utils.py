# ECE4424 Fake News Detection Project
# Topic - Utils
# Authors - Kevin Lizarazu
# Last Modified: 04/17/23

import json
import csv
import pandas as pd
import numpy as np
import string
import chardet
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
    readdata = pd.read_csv(file_path)

    # Lowercase the data
    cleandata = readdata.apply(lambda x: x.astype(str).str.lower())

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleandata['title'] = cleandata['title'].str.translate(translator)
    cleandata['text'] = cleandata['text'].str.translate(translator)

    # Returns the DataFrame with text that has been lowered and rid of punctutation
    return cleandata


##############################################################
# Testing Nonsense
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