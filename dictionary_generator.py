dictionary = {}
counter = 0
with open("Tree Stuff/processed_train_pos_data_no_label.txt") as f:
    text = f.read()
    for line in text:
        for word in line:
            for c in word:
                if c in dictionary.keys():
                    continue
                else:
                    dictionary[c] = counter
                    counter += 1
                    
with open("new_dict.pkl", "wb") as f:
    pickle.dump(dictionary,f)