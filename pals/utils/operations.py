import sys

from pals.utils.conversions import bytes_to_string

def fixed_xor(var_1: bytes, var_2: bytes) -> bytes:
    result = b''
    try:
        for a, b in zip(var_1, var_2):
            result += (a ^ b).to_bytes(1, 'big')
    except Exception as e:
        print(e)
        sys.exit(1)
    
    return result

def repeating_key_xor(plaintext: bytes, key: bytes) -> bytes:
    block_len = len(plaintext)
    key_len = len(key)
    padding = block_len % key_len
    block_key = key*(block_len//key_len) + key[:padding]
    return fixed_xor(plaintext, block_key)

if __name__ == "__main__":
    cipher = 'ETAOIN SHRDLU'.encode()
    print(bytes_to_string(fixed_xor(cipher, str('X'*len(cipher)).encode())))