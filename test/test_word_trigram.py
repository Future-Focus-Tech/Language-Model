import unittest
import os
from word_trigram import word_trigram

class TestWordTrigramMethods(unittest.TestCase):

    def test_wordTrigram_JSON_file_is_generating(self):
        word_trigram.generate_word_trigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("wordTrigram.json"), msg="File not exist.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestWordTrigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)