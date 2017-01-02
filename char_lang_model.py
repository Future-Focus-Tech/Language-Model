# -*- coding: utf-8 -*-

import io, math, json
import nltk
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
from preprocessor import utf8_to_ascii

tokenizer = RegexpTokenizer("[a-zA-Z-']+")

with io.open("sample.txt",'r',encoding='utf8') as utf_file:
    file_content = utf_file.read()

ascii_content = utf8_to_ascii(file_content)
word_tokens = tokenizer.tokenize(ascii_content)
all_char_bigrams = []

for word in word_tokens:
    bigrams = ngrams(word, 2, pad_left=True, pad_right=True, left_pad_symbol='<w>', right_pad_symbol="</w>")
    all_char_bigrams.append(bigrams)

print all_char_bigrams

with open("charBigram.json",mode='r') as json_file:
    trained_result = json.load(json_file)

for char_bigram in all_char_bigrams:
    for cgram in char_bigram:
        if str(cgram) in trained_result:
            print "found: " + str(cgram) + str(math.exp(trained_result[str(cgram)]))
        else:
            print "not found: " + str(cgram)