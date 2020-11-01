from os import urandom
import hashlib

password = input()
hash = hashlib.pbkdf2_hmac('sha256', password.encode(), urandom(16), 1000)
print(hash)
