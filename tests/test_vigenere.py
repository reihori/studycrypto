from studycrypto.vigenere import encrypt, decrypt


def test_encrypt():
    assert encrypt("Hello, World!", "KEY") == "Rijvs, Uyvjn!"


def test_decrypt():
    assert decrypt("Rijvs, Uyvjn!", "KEY") == "Hello, World!"
