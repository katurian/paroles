import os
print(os.getcwd())

import nltk
parsed = []

with open('gametranscript', 'r') as f: # open the short story and set it to the variable f
    sents = f.read().split(".") # read f (the short story) and split it into a list of sentences, set all of this equal to "sents"
    for sent in sents: # for each sentence in sents do the following:
        parsed.append(nltk.pos_tag(nltk.word_tokenize(sent))) # tokenize it, parse it, then send it to parsed = []

print(parsed)
