import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") # tests correct translation of Bonjour to Hello
        

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") # tests correct translation of Hello to Bonjour
        
unittest.main()