import unittest
import os, json
from char_bigram import char_bigram

class TestCharBigramMethods(unittest.TestCase):

    def test_charBigram_JSON_file_is_generating(self):
        char_bigram.generate_char_bigram_probability("mypet.txt")
        self.assertTrue(os.path.exists("charBigram.json"), msg="File not exist.")

    def test_bigram_log_probability_of_starting_a_word_with_particular_letter(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('<w>', 'A')"], -4.629862798578463, msg=None)
        self.assertAlmostEqual(data["('<w>', 'I')"], -2.1875157632092583, msg=None)
        self.assertAlmostEqual(data["('<w>', 'J')"], -5.3230099791384085, msg=None)
        self.assertAlmostEqual(data["('<w>', 'y')"], -6.016157159698354, msg=None)
        self.assertAlmostEqual(data["('<w>', 'o')"], -2.9716347219749304, msg=None)


    def test_bigram_log_probability_of_not_starting_a_word_with_particular_letter(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('<w>', 'z')" in data, msg="Starting letter exist.")
        self.assertFalse("('<w>', 'X')" in data, msg="Starting letter exist.")
        self.assertFalse("('<w>', 'C')" in data, msg="Starting letter exist.")
        self.assertFalse("('<w>', 'L')" in data, msg="Starting letter exist.")


    def test_bigram_log_probability_for_occurrence_of_two_characters_in_a_word(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('r', 'r')"], -3.7256934272366524, msg=None)
        self.assertAlmostEqual(data["('o', 'o')"], -3.9415818076696905, msg=None)
        self.assertAlmostEqual(data["('z', 'e')"], 0.0, msg=None)
        self.assertAlmostEqual(data["('l', 'y')"], -3.0602707946915624, msg=None)
        self.assertAlmostEqual(data["('a', 'n')"], -1.5702171992808192, msg=None)


    def test_bigram_log_probability_for_no_occurrence_of_two_characters_in_a_word(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('r', 'b')" in data, msg="Character combination exist.")
        self.assertFalse("('o', 'b')" in data, msg="Character combination exist.")
        self.assertFalse("('v', 'q')" in data, msg="Character combination exist.")
        self.assertFalse("('y', 'p')" in data, msg="Character combination exist.")
        self.assertFalse("('l', 'x')" in data, msg="Character combination exist.")

    def test_bigram_log_probability_of_ending_a_word_with_particular_letter(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertAlmostEqual(data["('d', '</w>')"], -0.4737843520856416, msg=None)
        self.assertAlmostEqual(data["('e', '</w>')"], -0.9886113934537812, msg=None)
        self.assertAlmostEqual(data["('r', '</w>')"], -1.5284688499004333, msg=None)
        self.assertAlmostEqual(data["('y', '</w>')"], -0.19671029424605427, msg=None)
        self.assertAlmostEqual(data["('a', '</w>')"], -2.3434070875143007, msg=None)

    def test_bigram_log_probability_of_not_ending_a_word_with_particular_letter(self):
        with open("charBigram.json") as data_file:
            data = json.load(data_file)
        self.assertFalse("('q', '</w>')" in data, msg="Ending letter exist.")
        self.assertFalse("('v', '</w>')" in data, msg="Ending letter exist.")
        self.assertFalse("('x', '</w>')" in data, msg="Ending letter exist.")
        self.assertFalse("('z', '</w>')" in data, msg="Ending letter exist.")


suite = unittest.TestLoader().loadTestsFromTestCase(TestCharBigramMethods)
unittest.TextTestRunner(verbosity=2).run(suite)