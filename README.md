# text-generation-GAN
IcGAN for generating text conditioned on certain sentiment. Stanford Sentiment Treebank. CS 224U Final Project

This project is based on the previous work of LantaoYu. https://github.com/LantaoYu/SeqGAN

## Download

1. Download SST dataset in this way....
2. Remove the zip files.
3. then simply run this command to turn SST PTB trees into sentences with corresponding sentiment label

## Preprocessing

## Training and such


# Setup


# Baseline

##Description
Our baseline (*baseline.py*) is built around a Laplacian estimate of relative sentiment frequency for a given word. *processed_train_data.txt* is utilized to build mappings of sentiment to relative word frequency - Each word's "score" is a Laplace-smoothed measure of the portion of times the word is observed with a given sentiment. In the baseline implementation, the model simply returns the set of n words with the highest score with a given sentiment flag (on a 0-4 scale). Output of the baseline is deterministic.

The baseline model delivers strong results with respect to true sentiment of a given string, but performs very poorly in terms of intelligence and grammar.

##Usage
>python baseline.py