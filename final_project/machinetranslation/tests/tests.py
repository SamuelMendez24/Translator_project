import unittest
from translator import fr_en, en_fr
class Testen_er(unittest.TestCase):
    def test1(self):
        self.assertEqual(en_fr('Hello'),'"Bonjour"')
        self.assertNotEqual(en_fr('Bonjour'),'"Hola"')        
        
class Testfr_en(unittest.TestCase):
    def test2(self):
        self.assertEqual(fr_en('Bonjour'),'"Hello"')
        self.assertNotEqual(fr_en('Hello'),'"hola"')
        
unittest.main()
