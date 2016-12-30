# -*- coding: utf-8 -*-

import io, json
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from preprocessor import utf8_to_ascii

with io.open("sample.txt",'r',encoding='utf8') as utf_file:
    file_content = utf_file.read()

ascii_content = utf8_to_ascii(file_content)
sentence_tokenize_list = sent_tokenize(ascii_content)

all_bigrams = []
trained_result = {}

for sentence in sentence_tokenize_list:
    sentence = sentence.rstrip('.!?')
    tokens = nltk.re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence)
    bigrams = ngrams(tokens, 2,pad_left=True,pad_right=True,left_pad_symbol='<s>', right_pad_symbol="</s>")
    all_bigrams.extend(bigrams)


with open("wordBigram.json",mode='r') as json_file:
    trained_result = json.load(json_file)

for bgram in all_bigrams:
    if str(bgram) in trained_result:
        print "found: " + str(bgram) + str(trained_result[str(bgram)])
    else:
        print "not found: " + str(bgram)

