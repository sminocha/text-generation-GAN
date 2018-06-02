import sys
import os
import math
import operator


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

pull_relations(total)
generate_sentence(sentiment=4, length=25)

