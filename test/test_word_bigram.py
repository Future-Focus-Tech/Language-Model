import unittest
import os, json
from word_bigram import word_bigram

class TestWordBigramMethods(unittest.TestCase):

    def test_wordBigram_JSON_file_is_generating(self):
        word_bigram.generate_word_bigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("wordBigram.json"), msg="File not exist.")


    def test_bigram_log_probability_of_starting_sentence_with_a_particular_word(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('<s>', 'A')"], -3.951243718581427, msg=None)
        self.assertAlmostEqual(data["('<s>', 'Occasionally')"], -3.951243718581427, msg=None)
        self.assertAlmostEqual(data["('<s>', 'It')"], -0.5839478885949533, msg=None)
        self.assertAlmostEqual(data["('<s>', 'At')"], -2.8526314299133175, msg=None)
        self.assertAlmostEqual(data["('<s>', 'I')"], -1.754019141245208, msg=None)

    def test_not_starting_sentence_with_a_particular_word(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('<s>', 'Be')" in data , msg="Starting word exist.")
        self.assertFalse("('<s>', 'Particularly')" in data , msg="Starting word exist.")
        self.assertFalse("('<s>', 'Asked')" in data , msg="Starting word exist.")
        self.assertFalse("('<s>', 'bottle')" in data , msg="Starting word exist.")
        self.assertFalse("('<s>', 'data')" in data , msg="Starting word exist.")

    def test_bigram_log_probability_for_occurence_of_word_pair_in_a_sentence(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('I', 'am')"], -1.9459101490553135, msg=None)
        self.assertAlmostEqual(data["('a', 'walk')"], -2.4849066497880004, msg=None)
        self.assertAlmostEqual(data["('and', 'long')"], -2.70805020110221, msg=None)
        self.assertAlmostEqual(data["('come', 'near')"], -0.6931471805599453, msg=None)
        self.assertAlmostEqual(data["('in', 'our')"], -1.3862943611198906, msg=None)


    def test_no_occurence_of_word_pair_in_a_sentence(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('am', 'I')" in data, msg="Starting word exist.")
        self.assertFalse("('walk', 'in')" in data, msg="Starting word exist.")
        self.assertFalse("('our', 'need')" in data, msg="Starting word exist.")
        self.assertFalse("('a', 'bottle')" in data, msg="Starting word exist.")
        self.assertFalse("('speed', 'at')" in data, msg="Starting word exist.")


    def test_bigram_log_probability_of_ending_sentence_with_a_particular_word(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('hunting', '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["('in', '</s>')"], -1.3862943611198906, msg=None)
        self.assertAlmostEqual(data["('walk', '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["('name', '</s>')"], 0.0, msg=None)
        self.assertAlmostEqual(data["('kitchen', '</s>')"], 0.0, msg=None)

    def test_not_ending_sentence_with_a_particular_word(self):
        with open("wordBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('they', '</s>')"in data , msg=None)
        self.assertFalse("('we', '</s>')"in data , msg=None)
        self.assertFalse("('could', '</s>')"in data , msg=None)
        self.assertFalse("('he', '</s>')"in data , msg=None)
        self.assertFalse("('going', '</s>')"in data , msg=None)



suite = unittest.TestLoader().loadTestsFromTestCase(TestWordBigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)