# Conspiracy Watch Tryout

Exploratory code for the project Conspiracy Watch, which is a data mining project with the goal of monitoring German conspiracy theorists acitivities on social media.

### Current state

The repository contains sample code for pulling data from telegram channels and tryouts of processing resulting text samples. The code is in an exploratory state and far from production-ready.

- Data is pulled from Telegram Channels (example used is the right-wing conspiracy channel @gerechtigkeitfuersvaterland), containing the text, view data, forwarding data, media data and some metadata
- Text is processed using spacy, extracting Named Entities, Tokens, Part-of-Speech sequences and channel referrals for graph mining
 