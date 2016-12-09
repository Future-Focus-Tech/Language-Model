# -*- coding: utf-8 -*-

import json


def utf8_to_ascii(utf8_text):
    with open("utf_to_ascii.json") as data_file:
        data = json.load(data_file)
    utf_table = data["chars"]
    for key, value in utf_table.items():
        utf8_text = utf8_text.replace(key, value)
    return utf8_text.encode('ascii')
