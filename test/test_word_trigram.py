import unittest
import os, json
from word_trigram import word_trigram

class TestWordTrigramMethods(unittest.TestCase):

    def test_wordTrigram_JSON_file_is_generating(self):
        word_trigram.generate_word_trigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("wordTrigram.json"), msg="File not exist.")

    def test_trigram_log_probability_for_starting_sentence_with_a_particular_word(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<s>', '<s>'), 'A')"], -3.951243718581427, msg=None)
        self.assertAlmostEqual(data["(('<s>', '<s>'), 'It')"], -0.5839478885949533, msg=None)
        self.assertAlmostEqual(data["(('<s>', '<s>'), 'I')"], -1.754019141245208, msg=None)
        self.assertAlmostEqual(data["(('<s>', '<s>'), 'To')"], -3.951243718581427, msg=None)
        self.assertAlmostEqual(data["(('<s>', '<s>'), 'At')"], -2.8526314299133175, msg=None)

    def test_not_starting_sentence_with_a_particular_given_word(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('<s>', '<s>'), 'Why')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', '<s>'), 'What')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', '<s>'), 'You')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', '<s>'), 'Pet')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', '<s>'), 'Dog')" in data, msg="Starting word exist.")


    def test_trigram_log_probability_for_sentence_to_start_with_given_word_pair(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('<s>', 'At'), 'night')"], -1.0986122886681098, msg=None)
        self.assertAlmostEqual(data["(('<s>', 'I'), 'am')"], -2.1972245773362196, msg=None)
        self.assertAlmostEqual(data["(('<s>', 'I'), 'have')"], -1.5040773967762742, msg=None)
        self.assertAlmostEqual(data["(('<s>', 'It'), 'accompanies')"], -3.367295829986474, msg=None)
        self.assertAlmostEqual(data["(('<s>', 'It'), 'has')"], -2.6741486494265287, msg=None)


    def test_not_to_start_a_sentence_with_given_word_pair(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('<s>', 'At'), 'Day')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', 'Am'), 'I')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', 'It'), 'gives')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', 'They'), 'say')" in data, msg="Starting word exist.")
        self.assertFalse("(('<s>', 'am'), 'the')" in data, msg="Starting word exist.")


    def test_trigram_log_probalility_for_sentence_having_three_word_consecutively(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('I', 'am'), 'fond')"], -0.6931471805599453, msg=None)
        self.assertAlmostEqual(data["(('It', 'runs'), 'at')"], -1.3862943611198906, msg=None)
        self.assertAlmostEqual(data["(('a', 'very'), 'strong')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('and', 'other'), 'small')"], -0.6931471805599453, msg=None)
        self.assertAlmostEqual(data["(('is', 'very'), 'beautiful')"], -1.0986122886681098, msg=None)

    def test_not_having_given_three_word_consecutively_in_sentence(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('I', 'am'), 'cool')" in data, msg="Starting word exist.")
        self.assertFalse("(('It', 'runs'), 'slow')" in data, msg="Starting word exist.")
        self.assertFalse("(('and', 'am'), 'pet')" in data, msg="Starting word exist.")
        self.assertFalse("(('It', 'runs'), 'and')" in data, msg="Starting word exist.")

    def test_trigram_log_probability_for_sentence_ending_with_given_word_pair(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["(('its', 'mouth'), '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('overtakes', 'them'), '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('soap', 'every-day'), '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["(('the', 'house'), '</s>')"], -0.2876820724517809, msg=None)
        self.assertAlmostEqual(data["(('to', 'sound'), '</s>')"], 0.0, msg=None)

    def test_sentence_not_ending_with_given_word_pair(self):
        with open("wordTrigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("(('am', 'i'), '</s>')" in data, msg="Starting word exist.")
        self.assertFalse("(('It', 'quits'), '</s>')" in data, msg="Starting word exist.")
        self.assertFalse("(('and', 'also'), '</s>')" in data, msg="Starting word exist.")
        self.assertFalse("(('It', 'sound'), '</s>')" in data, msg="Starting word exist.")


suite = unittest.TestLoader().loadTestsFromTestCase(TestWordTrigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)