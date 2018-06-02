from nltk.tree import Tree
import sst

data =[]
for y in sst.train_reader():
	sent = ""
	for tree in y:
		if type(tree) == Tree:
			sent = " ".join(tree.leaves())
		#else:
		#	sent += " " + str(tree)
	data.append(sent)

f = open("processed_train_data_no_label.txt", 'w+')
for sent in data:
	f.write(sent + "\n")