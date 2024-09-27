import itertools


def _vigenere(text: str, key: str, is_encrypt: bool) -> str:
    result_chars = []
    key_cycle = itertools.cycle(key.upper())
    for char in text:
        if not char.isalpha():
            result_chars.append(char)
            continue
        base = ord("a") if char.islower() else ord("A")
        shift = ord(next(key_cycle)) - ord("A")
        offset = (ord(char) - base + (shift if is_encrypt else -shift)) % 26
        result_char = chr(base + offset)
        result_chars.append(result_char)
    return "".join(result_chars)


def encrypt(text: str, key: str) -> str:
    return _vigenere(text, key, True)


def decrypt(text: str, key: str) -> str:
    return _vigenere(text, key, False)
