import unittest
import os
from word_bigram import word_bigram

class TestWordBigramMethods(unittest.TestCase):

    def test_wordBigram_JSON_file_is_generating(self):
        word_bigram.generate_word_bigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("wordBigram.json"), msg="File not exist.")

if __name__ == '__main__':
    unittest.main()