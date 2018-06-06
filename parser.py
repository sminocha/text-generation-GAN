from nltk.tree import Tree
#import pandas as pd
import sst

data =[]
for y in sst.train_reader():
	sent = ""
	for tree in y:
		if type(tree) == Tree:
			sent = " ".join(tree.leaves())
		else:
			if (int(tree) < 2):
			#sent += " " + str(tree)
				data.append(sent)

print(len(data))
f = open("processed_train_neg_data_no_label.txt", 'w+')
for sent in data:
	f.write(sent + "\n")
#train_labels = [y for tree, y in sst.train_reader()]