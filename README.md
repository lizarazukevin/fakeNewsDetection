# Fake News Detection

## Course
ECE 4424 - Machine Learning @ Virginia Tech

## Authors
Kevin Lizarazu-Ampuero <br>
Luc Phan

## Objective
In the age of mass media, it’s important to keep news reliable and trustworthy to prevent the following:
- Misinformation
- Targeted attacks
- Manipulation
- Phishing/malware attacks
- Reputation damage

This project will explore real world cybersecurity issues and the advancements of natural language processing.

## Classifiers
- Naive Bayes - Generative classifier
- Support Vector Machine (SVM) - Discriminative classifier
- ChatGPT - Large Language Model classifier

## Data Used to Train/Test
Provided by the course on Canvas, the train (39919 entries) and test(5000) datasets were both annotated CSV files that contained the following information:
- Title
- Text
- Subject
- Date

Labels were either real or fake, corresponding to if the news articles were honest and valid.
It is assumed that the training and testing files are named "train.csv" and "test.csv" respectively.

## Build and Run
This project contains util python files and jupyter notebooks that can be easily run, to see our results check out the following notebooks and run their cells:
- naiveBayes.ipynb
- svm.ipynb
It is expected that all packages in the jupyter notebooks be installed on the machine. This includes pandas, numpy, and several others.

Make sure that your environment has the correct dependencies by installing everything in the <i>requirements.txt</i>
```
pip install -r requirements.txt
```


All other configurables like paths can be found in <i>config.json</i>



