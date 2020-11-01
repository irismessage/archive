import hashlib
import sqlite3

class login:
    def __init__(self):
        self.users = 'users.txt'
        self.hasher = hashlib.pbkdf2_hmac
        
    def retrieve(users):
        with open(users, 'r') as database:
            return database.read()
    
    def save(users, file):
        with open(users, 'w') as database:
            database.write(file)
    
    def authenticate(self, username):
        users = retrieve(self.users)
        if username in users:
            
class database:
    def __init__(self, file, name, fields):
        self.file = file
        self.connection = sqlite.connect(self.file)
        self.cursor = self.connection.cursor()
        command = '''CREATE TABLE''' 
        
    