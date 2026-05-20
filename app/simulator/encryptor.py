import base64


def toy_encrypt(data: bytes) -> bytes:
    return base64.b64encode(data)



def toy_decrypt(data: bytes) -> bytes:
    return base64.b64decode(data)