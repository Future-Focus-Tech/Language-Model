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
all_char_bigrams = []

for word in word_tokens:
    bigrams = ngrams(word, 2, pad_left=True, pad_right=True, left_pad_symbol='<w>', right_pad_symbol="</w>")
    all_char_bigrams.extend(bigrams)

conditional_frequency_distribution = nltk.ConditionalFreqDist(all_char_bigrams)
conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

for bgram in all_char_bigrams:
    print "{0}: {1}".format(conditional_probability_distribution[bgram[0]].prob(bgram[1]), bgram)