# -*- coding: utf-8 -*-

import io, math, json
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

char_bigram_dict = {}

for bgram in all_char_bigrams:
    char_bigram_dict[str(bgram)] = math.log(conditional_probability_distribution[bgram[0]].prob(bgram[1]))
    print bgram, conditional_probability_distribution[bgram[0]].prob(bgram[1])

with open('charBigram.json', 'w+') as fp:
    json.dump(char_bigram_dict, fp, sort_keys=True, indent=4)