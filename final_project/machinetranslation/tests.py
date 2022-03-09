import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    """English to French tests"""
    def test1(self): 
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
    def test2(self):
        self.assertEqual(english_to_french('I love you'), "Je t'aime")
    def test3(self):
        self.assertNotEqual(english_to_french("None"), '')  
    def test4(self):  
        self.assertNotEqual(english_to_french(0), 0)
    def test5(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestF2E(unittest.TestCase): 
    """French to English tests"""
    def test1(self): 
        self.assertEqual(french_to_english('Comment vas-tu?'), 'How are you?')
    def test2(self):
        self.assertEqual(french_to_english('Je voudrais une pizza'), 'I want a pizza')  
    def test3(self):
        self.assertNotEqual(french_to_english("None"), '')    
    def test4(self):   
        self.assertNotEqual(french_to_english(0), 0)
    def test5(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()