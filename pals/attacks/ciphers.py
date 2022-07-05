import chunk
import string
from typing import Tuple, List

from pals.utils.operations import fixed_xor
from pals.utils.scorers import count_etaoi, frequency_histogram, hamming_distance, is_printable_ascii, count_char

def single_byte_xor_cipher_sapce_count(cipher: bytes) -> Tuple[str, bytes, int]:
    space_count = 0
    new_key = None
    new_plaintext = None
    for key in string.printable:
        plaintext = fixed_xor(cipher, str(key*len(cipher)).encode())
        if is_printable_ascii(plaintext):
            if count_char(plaintext) > space_count:
                new_key = key
                new_plaintext = plaintext
                space_count = count_char(plaintext)
    return new_key, new_plaintext, space_count

def single_byte_xor_cipher_histogram(cipher: bytes) -> Tuple[str, bytes, int]:
    etaoi_count = 0
    new_key = None
    new_plaintext = None
    for key in string.printable:
        plaintext = fixed_xor(cipher, str(key*len(cipher)).encode())
        if is_printable_ascii(plaintext):
            frequency = frequency_histogram(plaintext.decode())
            if count_etaoi(frequency) > etaoi_count:
                new_key = key
                new_plaintext = plaintext
                etaoi_count = count_etaoi(frequency)
    return new_key, new_plaintext, etaoi_count

def find_single_byte_xor_cipher(ciphers: List[bytes]) -> Tuple[bytes, str, bytes]:
    space_count = 0
    return_cipher = None
    key = None
    plaintext = None
    for cipher in ciphers:
        new_key, new_plaintext, new_space_count = single_byte_xor_cipher_sapce_count(cipher)
        if new_space_count > space_count:
            return_cipher = cipher
            key = new_key
            plaintext = new_plaintext
            space_count = new_space_count
    return return_cipher, key, plaintext

def repeating_key_xor_cipher(cipher: bytes) -> Tuple[bytes, bytes]:
    key = None
    plaintext = None
    key_len = 0
    ham_dist = 100.0
    chunks = 10

    for length in range(2, 40):
        normalised_hamming_distance = 0.0
        for i in range(0, chunks, 2):
            normalised_hamming_distance += hamming_distance(cipher[length*i:length*(i+1)], cipher[length*(i+1):length*(i+2)])/length
        normalised_hamming_distance = normalised_hamming_distance/(chunks/2)
        if normalised_hamming_distance < ham_dist:
            ham_dist = normalised_hamming_distance
            key_len = length
    
    cipher_blocks = []
    for i in range(key_len):
        cipher_block = b''
        for j in range(i, len(cipher), key_len):
            cipher_block += bytes([cipher[j]])
        cipher_blocks.append(cipher_block)

    for cipher_block in cipher_blocks:
        print(single_byte_xor_cipher_histogram(cipher_block))

    return key, plaintext


if __name__ == "__main__":
    print(single_byte_xor_cipher_sapce_count('ETAOIN SHRDLU'.encode()))
