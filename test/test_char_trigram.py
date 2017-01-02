import unittest
import os, json
from char_trigram import char_trigram

class TestCharTrigramMethods(unittest.TestCase):

    def test_charTrigram_JSON_file_is_generating(self):
        char_trigram.generate_char_trigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("charTrigram.json"), msg="File not exist.")

    def test_trigram_log_probability_of_starting_a_word_with_particular_letter(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'e')"], -4.629862798578463, msg="Starting letter not exist.")
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'm')"], -2.797281334830153, msg="Starting letter not exist.")
        self.assertAlmostEqual(data["(('<w>', 'a'), 'm')"], -3.2386784521643803, msg="Starting letter not exist.")
        self.assertAlmostEqual(data["(('<w>', 'f'), 'a')"], -2.3025850929940455, msg="Starting letter not exist.")
        self.assertAlmostEqual(data["(('<w>', 'e'), 'v')"], -0.6931471805599453, msg="Starting letter not exist.")

    def test_trigram_log_probability_of_not_starting_a_word_with_particular_letter(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('<w>', '<w>'), 'z')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'X')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'Z')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'Q')" in data, msg="Starting letter exist.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestCharTrigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)