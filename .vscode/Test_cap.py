import unittest
import Cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Python')