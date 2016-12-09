# -*- coding: utf-8 -*-

import io
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from preprocessor import utf8_to_ascii

with io.open("mypet.txt",'r',encoding='utf8') as utf_file:
    file_content = utf_file.read()

ascii_content = utf8_to_ascii(file_content)
sentence_tokenize_list = sent_tokenize(ascii_content)

trigrams_as_bigrams = []
for sentence in sentence_tokenize_list:
    sentence = sentence.rstrip('.!?')
    tokens = nltk.re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence)
    trigrams = ngrams(tokens, 3,pad_left=True,pad_right=True,left_pad_symbol='<s>', right_pad_symbol="</s>")
    trigrams_as_bigrams.extend([((t[0],t[1]), t[2]) for t in trigrams])

conditional_frequency_distribution = nltk.ConditionalFreqDist(trigrams_as_bigrams)
conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

for trigram in trigrams_as_bigrams:
    print "{0}: {1}".format(conditional_probability_distribution[trigram[0]].prob(trigram[1]), trigram)