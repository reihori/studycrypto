from studycrypto.caesar import encrypt, decrypt


def test_encrypt():
    assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"


def test_decrypt():
    assert decrypt("Khoor, Zruog!", 3) == "Hello, World!"
