import spacy
import json

nlp = spacy.load("de_core_news_sm")

def extract_data(telegram_data):
    '''Extract data from telegram json for a single post'''

    out = telegram_data
    doc = nlp(telegram_data['message'])
    out['tokens'] = [{
                        'text': token.text,
                        'lemma': token.lemma_,
                        'pos': token.pos_
                     } for token in doc]
    out['entities'] = [{
                            'text': ent.text,
                            'start': ent.start_char,
                            'end': ent.end_char,
                            'type': ent.label_
                       } for ent in doc.ents]
    channel_referrals = []
    for tok in out['tokens']:
        if tok['text'][0] == '@':
            channel_referrals.append(tok['text'])
    out['channel_referrals'] = channel_referrals
    return out

data = json.load(open('channel_messages.json', 'rb'))
sample = extract_data(data[300])
sample['entities']
sample['channel_referrals']