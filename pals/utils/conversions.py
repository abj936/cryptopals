from binascii import b2a_base64
from typing import List

def hex_str_to_bytes(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str)

def bytes_to_string(byte_str: bytes) -> str:
    return byte_str.decode()

def hex_to_base64(hex_str: str) -> str:
    return b2a_base64(hex_str_to_bytes(hex_str)).strip()

def file_byte_blob_to_list(blob: bytes) -> List[bytes]:
    return blob.splitlines()

def bytes_to_bin(text: bytes) -> bin:
    return bin(int(text.hex(), 16))