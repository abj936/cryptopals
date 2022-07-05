from operator import index
import unittest

from pals.attacks.ciphers import single_byte_xor_cipher_sapce_count, find_single_byte_xor_cipher, repeating_key_xor_cipher
from pals.utils.conversions import hex_str_to_bytes, bytes_to_string
from pals.utils.io import read_hex_list_from_file, read_base64_blob_from_file

class TestCipherAttacks(unittest.TestCase):
    def test_single_byte_xor_cipher(self):
        cipher = hex_str_to_bytes('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
        key, plaintext, _ = single_byte_xor_cipher_sapce_count(cipher)
        self.assertEqual(key, 'X')
        self.assertEqual(bytes_to_string(plaintext), "Cooking MC's like a pound of bacon")

    def test_find_single_byte_xor_cipher(self):
        fname = 'tests/samples/hidden_single_byte_xor_cipher.txt'
        ciphers = read_hex_list_from_file(fname)
        cipher, key, plaintext = find_single_byte_xor_cipher(ciphers)
        self.assertEqual(cipher, hex_str_to_bytes('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f'))
        self.assertEqual(key, '5')
        self.assertEqual(bytes_to_string(plaintext), 'Now that the party is jumping\n')

    def test_repeating_key_xor_cipher(self):
        fname = 'tests/samples/base64_repeating_key_xor_cipher.txt'
        cipher = read_base64_blob_from_file(fname)
        key, plaintext = repeating_key_xor_cipher(cipher)
        self.assertEqual(key, 'key')
        self.assertEqual(bytes_to_string(plaintext), 'plaintext')


if __name__ == "__main__":
    unittest.main()