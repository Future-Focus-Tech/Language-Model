# -*- coding: utf-8 -*-

import io
import nltk
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
from preprocessor import utf8_to_ascii

tokenizer = RegexpTokenizer("[a-zA-Z-']+")

with io.open("mypet.txt",'r',encoding='utf8') as utf_file:
    file_content = utf_file.read()

ascii_content = utf8_to_ascii(file_content)
word_tokens = tokenizer.tokenize(ascii_content)
char_trigram_as_bigram = []

for word in word_tokens:
    trigrams = ngrams(word, 3, pad_left=True, pad_right=True, left_pad_symbol='<w>', right_pad_symbol="</w>")
    char_trigram_as_bigram.extend([((t[0],t[1]), t[2]) for t in trigrams])

conditional_frequency_distribution = nltk.ConditionalFreqDist(char_trigram_as_bigram)
conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

for tgram in char_trigram_as_bigram:
    print "{0}: {1}".format(conditional_probability_distribution[tgram[0]].prob(tgram[1]), tgram)