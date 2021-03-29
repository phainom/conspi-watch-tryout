### Script to show possible enrichment of data based on a sample channel ('gerechtigkeitfuersvaterland')

import json
from flair.data import Sentence
from flair.models import SequenceTagger


data = json.load(open('channel_messages.json', 'rb'))
len(data)
text = data[0]['message']

# make a sentence
sentence = Sentence(text)

# load the NER tagger
tagger = SequenceTagger.load('de-ner')

# run NER over sentence
tagger.predict(sentence)
for entity in sentence.get_spans('ner'):
    print(entity)