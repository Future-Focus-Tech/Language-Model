import unittest
import os
from char_trigram import char_trigram

class TestCharTrigramMethods(unittest.TestCase):

    def test_charTrigram_JSON_file_is_generating(self):
        char_trigram.generate_char_trigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("charTrigram.json"), msg="File not exist.")

if __name__ == '__main__':
    unittest.main()