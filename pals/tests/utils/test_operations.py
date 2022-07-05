import unittest
from pals.utils.operations import fixed_xor, repeating_key_xor
from pals.utils.conversions import hex_str_to_bytes

class TestOperations(unittest.TestCase):
    def test_fixed_xor(self):
        self.assertEqual(
            fixed_xor(
                hex_str_to_bytes('1c0111001f010100061a024b53535009181c'),
                hex_str_to_bytes('686974207468652062756c6c277320657965')),
            hex_str_to_bytes('746865206b696420646f6e277420706c6179'))

    def test_repeating_key_xor(self):
        plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        key = b'ICE'
        self.assertEqual(
            repeating_key_xor(plaintext, key).hex(),
            '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272' \
            'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
        )
        

if __name__ == "__main__":
    unittest.main()
