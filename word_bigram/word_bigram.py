# -*- coding: utf-8 -*-

import math, json
import nltk
from nltk.util import ngrams
from utilities import get_sentence_tokens


def get_all_word_bigrams(corpus_file):
    sentence_tokenize_list = get_sentence_tokens(corpus_file)

    all_bigrams = []

    for sentence in sentence_tokenize_list:
        sentence = sentence.rstrip('.!?')
        tokens = nltk.re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence)
        bigrams = ngrams(tokens, 2,pad_left=True,pad_right=True,left_pad_symbol='<s>', right_pad_symbol="</s>")
        all_bigrams.extend(bigrams)
    return all_bigrams


def generate_word_bigram_probability(corpus_file):
    all_bigrams = get_all_word_bigrams(corpus_file)
    conditional_frequency_distribution = nltk.ConditionalFreqDist(all_bigrams)
    conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

    word_bigram_dict = {}

    for bgram in all_bigrams:
        word_bigram_dict[str(bgram)] = math.log(conditional_probability_distribution[bgram[0]].prob(bgram[1]))

    with open('wordBigram.json', 'w+') as fp:
        json.dump(word_bigram_dict, fp, sort_keys=True, indent=4)