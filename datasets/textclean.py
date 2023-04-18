import pandas as pd
# import numpy as np
import string


def main():
    # Read CSV
    readdata = pd.read_csv("train.csv")

    # DEBUG PRINTS
    # print("Uncleaned: ")
    # print(readdata['text'])

    # Lowercase the data
    cleandata = readdata.apply(lambda x: x.astype(str).str.lower())

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleandata['title'] = cleandata['title'].str.translate(translator)
    cleandata['text'] = cleandata['text'].str.translate(translator)

    # DEBUG PRINTS
    # print("Cleaned: ")
    # print(cleandata['text'])

    # Write to new csv file
    cleandata.to_csv("cleanedtrain.csv")


if __name__ == "__main__":
    main()
