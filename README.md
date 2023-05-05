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

## Build and Run
This project contains util python files and jupyter notebooks that can be easily run, to see our results check out the following notebooks and run their cells:
- naiveBayes.ipynb
- svm.ipynb

All other configurables like paths can be found in <i>config.json</i>



