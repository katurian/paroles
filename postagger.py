import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

def pos(text_file):
    pos_dict = {'adjectives': [], 'verbs': [], 'nouns': [], 'adverbs': [], 'proper_nouns': [], 'pronouns': [],
                'subjects': [], 'direct_objects': [], 'indirect_objects': [], 'symbols': [], 'numbers': []}
    with open(text_file, encoding='utf8', errors='ignore') as f:
        text = nlp(f.read())
        for token in text:
                if token.pos_ == "ADJ":
                    pos_dict["adjectives"].append(token.text)
                if token.pos_ == "VERB":
                    pos_dict["verbs"].append(token.text)
                if token.pos_ == "ADV":
                    pos_dict["adverbs"].append(token.text)
                if token.pos_ == "NOUN":
                    pos_dict["nouns"].append(token.text)
                if token.pos_ == "PROPN":
                    pos_dict["proper_nouns"].append(token.text)
                if token.pos_ == "NUM":
                    pos_dict["numbers"].append(token.text)
                if token.pos_ == "SYM":
                    pos_dict["symbols"].append(token.text)
                if token.pos_ == "PRON":
                    pos_dict["pronouns"].append(token.text)
                if token.dep_ == "dobj":
                    direct_object = token.orth_
                    pos_dict["direct_objects"].append(direct_object)
                if token.dep_ == "iobj":
                    indirect_object = token.orth_
                    pos_dict["indirect_objects"].append(indirect_object)
                if token.dep_ == "nsubj":
                    subject = token.orth_
                    pos_dict["subjects"].append(subject)
        return pos_dict
    
pos("corpus.txt")
