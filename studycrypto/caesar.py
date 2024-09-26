def encrypt(text: str, shift: int) -> str:
    encrypted_chars = []
    for char in text:
        if not char.isalpha():
            encrypted_chars.append(char)
            continue
        base = ord("a") if char.islower() else ord("A")
        offset = (ord(char) - base + shift) % 26
        encrypted_char = chr(base + offset)
        encrypted_chars.append(encrypted_char)
    return "".join(encrypted_chars)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
