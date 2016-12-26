# -*- coding: utf-8 -*-

import io, math, json
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from preprocessor import utf8_to_ascii

with io.open("mypet.txt",'r',encoding='utf8') as utf_file:
    file_content = utf_file.read()

ascii_content = utf8_to_ascii(file_content)
sentence_tokenize_list = sent_tokenize(ascii_content)

all_bigrams = []

for sentence in sentence_tokenize_list:
    sentence = sentence.rstrip('.!?')
    tokens = nltk.re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence)
    bigrams = ngrams(tokens, 2,pad_left=True,pad_right=True,left_pad_symbol='<s>', right_pad_symbol="</s>")
    all_bigrams.extend(bigrams)

conditional_frequency_distribution = nltk.ConditionalFreqDist(all_bigrams)
conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

word_bigram_dict = {}

for bgram in all_bigrams:
    word_bigram_dict[str(bgram)] = math.log10(conditional_probability_distribution[bgram[0]].prob(bgram[1]))

with open('wordBigram.json', 'w+') as fp:
    json.dump(word_bigram_dict, fp, sort_keys=True, indent=4)