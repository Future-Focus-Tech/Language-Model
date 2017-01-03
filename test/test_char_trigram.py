import unittest
import os, json
from char_trigram import char_trigram

class TestCharTrigramMethods(unittest.TestCase):

    def test_charTrigram_JSON_file_is_generating(self):
        char_trigram.generate_char_trigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("charTrigram.json"), msg="File not exist.")

    def test_trigram_log_probability_of_starting_a_word_with_particular_single_character(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'e')"], -4.629862798578463, msg=None)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'm')"], -2.797281334830153, msg=None)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'd')"], -4.2243976904702984, msg=None)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'V')"], -6.016157159698354, msg=None)
        self.assertAlmostEqual(data["(('<w>', '<w>'), 'r')"], -3.9367156180185177, msg=None)

    def test_word_not_starting_with_particular_single_character(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('<w>', '<w>'), 'z')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'X')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'Z')" in data, msg="Starting letter exist.")
        self.assertFalse("(('<w>', '<w>'), 'Q')" in data, msg="Starting letter exist.")


    def test_trigram_log_probability_of_occurence_of_character_pair_in_a_word(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<w>', 'a'), 'b')"], -3.9318256327243257, msg=None)
        self.assertAlmostEqual(data["(('<w>', 'i'), 't')"], -0.6931471805599453, msg=None)
        self.assertAlmostEqual(data["(('<w>', 's'), 'l')"], -2.3025850929940455, msg=None)
        self.assertAlmostEqual(data["(('<w>', 's'), 't')"], -1.8971199848858813, msg=None)
        self.assertAlmostEqual(data["(('<w>', 'w'), 'o')"], -2.833213344056216, msg=None)


    def test_no_occurence_of_given_character_pair_in_a_word(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('<w>', 'a'), 'o')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('<w>', 'i'), 'y')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('<w>', 'z'), 's')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('<w>', 'q'), 'r')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('<w>', 'p'), 'g')" in data, msg="Starting character pair exist.")


    def test_trigram_log_probalility_for_occurence_of_three_consecutive_characters_in_a_word(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('a', 'b'), 'l')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('b', 'o'), 'd')"], -0.6931471805599453, msg=None)
        self.assertAlmostEqual(data["(('c', 'e'), 'i')"], -1.3862943611198906, msg=None)
        self.assertAlmostEqual(data["(('e', 'a'), 'u')"], -2.3025850929940455, msg=None)
        self.assertAlmostEqual(data["(('e', 'r'), 'a')"], -3.258096538021482, msg=None)


    def test_no_occurence_of_three_given_consecutive_characters_in_a_word(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('a', 'b'), 'c')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('b', 'o'), 'g')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('f', 'z'), 'e')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('z', 'q'), 'p')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('m', 'p'), 'y')" in data, msg="Starting character pair exist.")


    def test_trigram_log_probability_of_ending_a_word_with_given_character_pair(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('f', 't'), '</w>')"], -1.3862943611198906, msg=None)
        self.assertAlmostEqual(data["(('h', 'o'), '</w>')"], -2.1972245773362196, msg=None)
        self.assertAlmostEqual(data["(('k', 'e'), '</w>')"], -0.2876820724517809, msg=None)
        self.assertAlmostEqual(data["(('t', 'y'), '</w>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('o', 'k'), '</w>')"], -1.0986122886681098, msg=None)


    def test_not_ending_a_word_with_given_character_pair(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('a', 'b'), '</w>')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('b', 'o'), '</w>')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('f', 'z'), '</w>')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('z', 'q'), '</w>')" in data, msg="Starting character pair exist.")
        self.assertFalse("(('m', 'p'), '</w>')" in data, msg="Starting character pair exist.")


    def test_trigram_log_probability_of_starting_and_ending_a_word_with_particular_character(self):
        with open("charTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<w>', 'a'), '</w>')"], -1.4469189829363254, msg=None)
        self.assertAlmostEqual(data["(('<w>', 'I'), '</w>')"], -1.1895840668738362, msg=None)
        self.assertAlmostEqual(data["(('<w>', 'A'), '</w>')"], -1.3862943611198906, msg=None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCharTrigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)