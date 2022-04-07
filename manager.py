from email import message
import string
from cryptography.fernet import Fernet

def encrypt(message: string, key: string) -> bytes:
    message = bytes(message, 'utf8')
    key = bytes(key, 'utf8')
    return Fernet(key).encrypt(message)

def decrypt(token: string, key: string) -> bytes:
    token = bytes(token, 'utf8')
    key = bytes(key, 'utf8')
    return Fernet(key).decrypt(token)