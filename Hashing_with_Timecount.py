import random
import string
import bcrypt
from argon2 import PasswordHasher
import os
import time
def generate_passwords(count=10000, min_len=8, max_len=12):
    passwords = []
    for _ in range(count):
        length = random.randint(min_len, max_len)
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        passwords.append(password)
    return passwords
def hash_passwords_bcrypt(passwords):
    print("Starting bcrypt hashing...")
    start_time = time.time()
    hashed_passwords = []
    for pwd in passwords:
        hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
        hashed_passwords.append(hashed.decode('utf-8'))
    end_time = time.time()
    print(f"Bcrypt hashing completed. Time taken: {end_time - start_time:.2f} seconds.")
    return hashed_passwords
def hash_passwords_argon2(passwords):
    print("Starting Argon2 hashing...")
    ph = PasswordHasher()
    start_time = time.time()
    hashed_passwords = []
    for pwd in passwords:
        hashed = ph.hash(pwd)
        hashed_passwords.append(hashed)
    end_time = time.time()
    print(f"Argon2 hashing completed. Time taken: {end_time - start_time:.2f} seconds.")
    return hashed_passwords
def save_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for line in data:
                file.write(line + '\n')
        print(f"File saved successfully: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error saving file: {e}")
if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")   
    print("Generating passwords...")
    passwords = generate_passwords()
    print("Password generation completed. Saving plain passwords to file.")
    save_to_file("plain_passwords.txt", passwords)
    bcrypt_hashed = hash_passwords_bcrypt(passwords)
    save_to_file("bcrypt_hashed_passwords.txt", bcrypt_hashed)
    argon2_hashed = hash_passwords_argon2(passwords)
    save_to_file("argon2_hashed_passwords.txt", argon2_hashed)
    print("All tasks completed. Files saved in the current directory.")
