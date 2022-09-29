""" Unit tests for translator """
import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """ English to French unit test class"""
    def test1(self):
        """ English to French unit test method """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Enemy"), "Ami")
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french(""), "")


class TestF2E(unittest.TestCase):
    """ French to English unit test class"""
    def test1(self):
        """ French to English unit test method """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Howdy")
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english(""), "")

unittest.main()
