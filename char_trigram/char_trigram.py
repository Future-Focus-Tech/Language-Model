# -*- coding: utf-8 -*-

import math, json
import nltk
from nltk.util import ngrams
from utilities import get_word_tokens


def get_all_char_trigrams_as_bigram(corpus_file):
    word_tokens = get_word_tokens(corpus_file)
    char_trigram_as_bigram = []

    for word in word_tokens:
        trigrams = ngrams(word, 3, pad_left=True, pad_right=True, left_pad_symbol='<w>', right_pad_symbol="</w>")
        char_trigram_as_bigram.extend([((t[0],t[1]), t[2]) for t in trigrams])

    return char_trigram_as_bigram


def generate_char_trigram_probability(corpus_file):
    char_trigram_as_bigram = get_all_char_trigrams_as_bigram(corpus_file)
    conditional_frequency_distribution = nltk.ConditionalFreqDist(char_trigram_as_bigram)
    conditional_probability_distribution = nltk.ConditionalProbDist(conditional_frequency_distribution, nltk.MLEProbDist)

    char_trigram_dict = {}

    for tgram in char_trigram_as_bigram:
        char_trigram_dict[str(tgram)] = math.log(conditional_probability_distribution[tgram[0]].prob(tgram[1]))

    with open('charTrigram.json', 'w+') as fp:
        json.dump(char_trigram_dict, fp, sort_keys=True, indent=4)
