import unittest
import os
from char_bigram import char_bigram

class TestCharBigramMethods(unittest.TestCase):

    def test_charBigram_JSON_file_is_generating(self):
        char_bigram.generate_char_bigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("charBigram.json"), msg="File not exist.")

if __name__ == '__main__':
    unittest.main()