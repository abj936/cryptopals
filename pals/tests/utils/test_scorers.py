import unittest

from pals.utils.scorers import is_ascii, hamming_distance

class TestScorers(unittest.TestCase):
    def test_ascii_scorer(self):
        text = 'The quick brown fox, jumped over the lazy dog!'
        self.assertTrue(is_ascii(text))

    def test_hamming_distance(self):
        text_1 = b'this is a test'
        text_2 = b'wokka wokka!!!'
        self.assertEqual(hamming_distance(text_1, text_2), 37)

if __name__ == '__main__':
    unittest.main()