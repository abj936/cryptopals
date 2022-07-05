from typing import List
import base64

def read_hex_blob_from_file(fname: str) -> bytes:
    with open(fname, 'r') as f:
        return bytes.fromhex(f.read())

def read_hex_list_from_file(fname: str) -> List[bytes]:
    with open(fname, 'r') as f:
        data = f.read().splitlines()
    result = []
    for line in data:
        result.append(bytes.fromhex(line))
    return result

def read_base64_blob_from_file(fname: str) -> bytes:
    with open(fname, 'r') as f:
        data = f.read().splitlines()
    return base64.b64decode(''.join(data))

def read_blob_from_file(fname: str) -> str:
    with open(fname, 'r') as f:
        data = f.read().splitlines()
    return ''.join(data)