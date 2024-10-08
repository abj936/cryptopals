import unittest
from pals.utils.conversions import hex_to_base64, bytes_to_string

class TestConversions(unittest.TestCase):
    def test_hex_to_base64(self):
        self.assertEqual(bytes_to_string(hex_to_base64(
            '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')), 
            'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

if __name__ == "__main__":
    unittest.main()