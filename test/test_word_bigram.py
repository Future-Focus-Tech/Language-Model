import unittest
import os
from word_bigram import word_bigram

class TestWordBigramMethods(unittest.TestCase):

    def test_wordBigram_JSON_file_is_generating(self):
        word_bigram.generate_word_bigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("wordBigram.json"), msg="File not exist.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestWordBigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)