# Introduction
postagger.py (at the very bottom of the repository) opens a .txt file, tags each word in that file with a POS (parts of speech) label, and then appends each labeled word to its corresponding list. 

For example, here is a passage from Haruki Murakami's *Norwegian Wood*:

*I was thirty-seven then, strapped in my seat as the huge 747 plunged through dense cloud cover on approach to the Hamburg airport. Cold November rains drenched the earth and lent everything the gloomy air of a Flemish landscape: the ground crew in rain gear, a flag atop a squat airport building, a BMW billboard. So—Germany again. Once the plane was on the ground, soft music began to flow from the ceiling speakers: a sweet orchestral cover version of the Beatles’ “Norwegian Wood.” The melody never failed to send a shudder through me, but this time it hit me harder than ever. She smiled and left, and the music changed to a Billy Joel tune. I straightened up and looked out the plane window at the dark clouds hanging over the North Sea, thinking of what I had lost in the course of my life: times gone forever, friends who had died or disappeared, feelings I would never know again.*

And some of the lists postagger.py would generate from the text:

**adjectives**

['my', 'huge', 'dense', 'gloomy', 'Flemish', 'squat', 'soft', 'sweet', 'orchestral', 'dark', 'my']

**numbers**

['thirty', 'seven', '747']

**verbs**

['was', 'strapped', 'plunged', 'drenched', 'lent', 'was', 'began', 'flow', 'speakers', 'failed', 'send', 'hit', 'smiled', 'left', 'changed', 'straightened', 'looked', 'hanging', 'had', 'lost', 'gone', 'had', 'died', 'disappeared', 'would', 'know']

**nouns**

['seat', 'cloud', 'cover', 'approach', 'airport', 'rains', 'earth', 'everything', 'air', 'landscape', 'ground', 'crew', 'rain', 'gear', 'flag', 'airport', 'building', 'billboard', 'plane', 'ground', 'music', 'ceiling', 'cover', 'version', 'melody', 'shudder', 'time', 'music', 'tune', 'plane', 'window', 'clouds', 'thinking', 'what', 'course', 'life', 'times', 'friends', 'who', 'feelings']

**proper nouns**

['Hamburg', 'Cold', 'November', 'BMW', 'Germany', 'Beatles’', 'Norwegian', 'Wood', 'Billy', 'Joel', 'North', 'Sea']

**direct objects**

['earth', 'everything', 'air', 'version', 'shudder', 'me', 'window', 'what', 'feelings']

**adverbs**

['then', 'So', 'again', 'never', 'harder', 'ever', 'forever', 'never', 'again']


# Directions
1.  Install the **spaCy** package with **pip install spacy**.
2.  In your command-line interpreter, type **python -m spacy download en**, this downloads an English language model needed for the program to work: https://spacy.io/usage/models
3.  When you call the function **pos()** be sure to change 'gametranscript' to 'whatevertextfile.txt' you want to use. And make sure this txt file is in the same folder as postagger.py
4.  If you want to change the names of the POS lists in postagger.py, change them *after* line 45.
5. Run it!

I provided some corpora for you to play with. Take a look at Spacey's docs as well for new features you can add: https://spacy.io/usage/linguistic-features
