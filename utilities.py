# -*- coding: utf-8 -*-

import io, json
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer


def utf8_to_ascii(utf8_text):
    with open("utf_to_ascii.json") as data_file:
        data = json.load(data_file)
    utf_table = data["chars"]
    for key, value in utf_table.items():
        utf8_text = utf8_text.replace(key, value)
    return utf8_text.encode('ascii')


def get_ascii_content_from_file(file):
    with io.open(file, 'r', encoding='utf8') as utf_file:
        file_content = utf_file.read()
    return utf8_to_ascii(file_content)


def get_sentence_tokens(corpus_file):
    ascii_content = get_ascii_content_from_file(corpus_file)
    return sent_tokenize(ascii_content)


def get_word_tokens(corpus_file):
    tokenizer = RegexpTokenizer("[a-zA-Z-']+")
    ascii_content = get_ascii_content_from_file(corpus_file)
    return tokenizer.tokenize(ascii_content)
