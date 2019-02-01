import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

verb = []
adj = []
noun = []
adv = []
sub = []
dobj = []
iobj = []
pron = []
prop = []
sym = []
num = []

def pos(text):
    text = nlp(text)
    for token in text:
            if token.pos_ == "ADJ":
                adj.append(token.text)
            if token.pos_ == "VERB":
                verb.append(token.text)
            if token.pos_ == "ADV":
                adv.append(token.text)
            if token.pos_ == "NOUN":
                noun.append(token.text)
            if token.pos_ == "PROPN":
                prop.append(token.text)
            if token.pos_ == "NUM":
                num.append(token.text)
            if token.pos_ == "SYM":
                sym.append(token.text)
            if token.pos_ == "PRON":
                pron.append(token.text)
            if token.dep_ == "dobj":
                direct_object = token.orth_
                dobj.append(direct_object)
            if token.dep_ == "iobj":
                indirect_object = token.orth_
                iobj.append(indirect_object)
            if token.dep_ == "nsubj":
                subject = token.orth_
                sub.append(subject)


pos("I was thirty-seven then, strapped in my seat as the huge 747 plunged through dense cloud cover on approach to the Hamburg airport. Cold November rains drenched the earth and lent everything the gloomy air of a Flemish landscape: the ground crew in rain gear, a flag atop a squat airport building, a BMW billboard. So—Germany again. Once the plane was on the ground, soft music began to flow from the ceiling speakers: a sweet orchestral cover version of the Beatles’ “Norwegian Wood.” The melody never failed to send a shudder through me, but this time it hit me harder than ever. She smiled and left, and the music changed to a Billy Joel tune. I straightened up and looked out the plane window at the dark clouds hanging over the North Sea, thinking of what I had lost in the course of my life: times gone forever, friends who had died or disappeared, feelings I would never know again.")

text = ("I was thirty-seven then, strapped in my seat as the huge 747 plunged through dense cloud cover on approach to the Hamburg airport. Cold November rains drenched the earth and lent everything the gloomy air of a Flemish landscape: the ground crew in rain gear, a flag atop a squat airport building, a BMW billboard. So—Germany again. Once the plane was on the ground, soft music began to flow from the ceiling speakers: a sweet orchestral cover version of the Beatles’ “Norwegian Wood.” The melody never failed to send a shudder through me, but this time it hit me harder than ever. She smiled and left, and the music changed to a Billy Joel tune. I straightened up and looked out the plane window at the dark clouds hanging over the North Sea, thinking of what I had lost in the course of my life: times gone forever, friends who had died or disappeared, feelings I would never know again.")
print(text)
print(' ')
print(' ')
print('adjectives')
print(adj)
print(' ')
print('numbers')
print(num)
print(' ')
print('verbs')
print(verb)
print(' ')
print('nouns')
print(noun)
print(' ')
print('proper nouns')
print(prop)
print(' ')
print('direct objects')
print(dobj)
print(' ')
print('indirect objects')
print(iobj)
print(' ')
print('adverbs')
print(adv)
print(' ')
