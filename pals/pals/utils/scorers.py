import string
from typing import Dict
from collections import defaultdict

from pals.utils.conversions import bytes_to_bin
from pals.utils.io import read_blob_from_file
from pals.utils.operations import fixed_xor

def is_ascii(text: bytes) -> bool:
    return text.isascii()

def is_printable_ascii(text: bytes) -> bool:
    for char in text:
        if chr(char) not in string.printable:
            return False
    return True

def count_char(text: bytes, char = b' ') -> int:
    return text.count(char)

def count_etaoi(frequency: Dict) -> int:
    result = 0
    for char in 'eEtTaAoOiI':
        result  += frequency[char]
    return result

def hamming_distance(text_1: bytes, text_2: bytes) -> int:
    return bytes_to_bin(fixed_xor(text_1, text_2)).count('1')

def frequency_histogram(text: str) -> Dict:
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

if __name__ == '__main__':
    fname = 'tests/samples/alice_in_wonderland.txt'
    text = read_blob_from_file(fname)
    print(frequency_histogram(text))
    