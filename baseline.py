import sys
import os
import math
import operator
import argparse

featureMap = {}
sentCounts = {}
allWords = {}
total = 0


def pull_relations(total):
    filepath = "processed_train_data.txt"
    with open(filepath, "r") as f:
        for line in f:
            if len(line)>1:
                features = line.split(' ')
                sentiment = int(features[-1])
                features = features[:-1]
                if sentiment in featureMap:
                    loc = featureMap[sentiment]
                else:
                    loc = {}

                for feat in features:
                    total+=1
                    if feat in loc:
                        loc[feat] += 1.0
                    else:
                        loc[feat] = 1.0
                    if feat not in allWords:
                        allWords[feat] = 1.0
                    else:
                        allWords[feat] += 1.0

                featureMap[sentiment] = loc


    for sent in featureMap:
        for word in featureMap[sent]:
            #print(word)
            #print(featureMap[sent][word])
            adjusted_val = (float(featureMap[sent][word])+1) / (float(allWords[word])+len(featureMap))
            #prevalence = float(allWords[word]) / float(total)
            #logged = math.log(adjusted_val, 2)
            #print(logged)
            #print(prevalence)
            featureMap[sent][word] = adjusted_val

    #print(featureMap, total)


def generate_sentence(sentiment=4, length=5):
    localD = featureMap[sentiment]
    out = {key: localD[key] for key in sorted(localD, key=localD.get, reverse=True)[:length]}
    wordsToAdd = [word for word in out.keys()]
    review = ' '.join(wordsToAdd).lower()
    print(review)

parser = argparse.ArgumentParser(description='Flag and select sentiment/number of words')
parser.add_argument("--s", help="Set sentiment")
parser.add_argument("--n", help="Set numWords")
args = parser.parse_args()
sentiment = 4
numWords = 25
if args.s:
    sentiment = int(args.s)
if args.n:
    numWords = int(args.n)

if sentiment>4 or sentiment<0 or numWords<1:
    print("Error! Sentiment/Num Words flags out of bounds.")
    print("Refer to README.md for further instructions.")
    sys.exit(0)
pull_relations(total)
generate_sentence(sentiment=sentiment, length=numWords)