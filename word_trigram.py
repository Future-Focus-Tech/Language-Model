# -*- coding: utf-8 -*-

import math, json
import nltk
from nltk.util import ngrams
from utilities import get_sentence_tokens

sentence_tokenize_list = get_sentence_tokens("mypet.txt")

trigrams_as_bigrams = []
for sentence in sentence_tokenize_list:
    sentence = sentence.rstrip('.!?')
    tokens = nltk.re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence)
    trigrams = ngrams(tokens, 3,pad_left=True,pad_right=True,left_pad_symbol='<s>', right_pad_symbol="</s>")
    trigrams_as_bigrams.extend([((t[0],t[1]), t[2]) for t in trigrams])

conditional_frequency_distribution = nltk.ConditionalFreqDist(trigrams_as_bigrams)
conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

word_trigram_dict = {}

for trigram in trigrams_as_bigrams:
    word_trigram_dict[str(trigram)] = math.log(conditional_probability_distribution[trigram[0]].prob(trigram[1]))

with open('wordTrigram.json', 'w+') as fp:
    json.dump(word_trigram_dict, fp, sort_keys=True, indent=4)