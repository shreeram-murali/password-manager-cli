from cryptography.fernet import Fernet

class Passwords:
    def __init__(self, username, token) -> None:
        self._username = username
        self._token = token
    
    def encrypt(self, message: bytes, key: bytes) -> bytes:
        return Fernet(key).encrypt(message)

    def decrypt(self, token: bytes, key: bytes) -> bytes:
        return Fernet(key).decrypt(token)
