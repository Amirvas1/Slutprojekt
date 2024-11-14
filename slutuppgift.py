import argparse
from pathlib import Path
from cryptography.fernet import Fernet
import os

def generate_key(key_file_name):
    key = Fernet.generate_key()
    print(f"The key {key} is generated!")
    with open(key_file_name, "wb") as key_file:
        key_file.write(key)
    print(f"The key is saved and stored in: {key_file_name}")

def encrypted_mode(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()
        print(f"The key {key} is now open")

    cipher_suite = Fernet(key)

    with open(file, "rb") as encrypted_file:
        content = encrypted_file.read()
        cipher_content = cipher_suite.encrypt(content)
        
    with open(file, "wb") as encrypted_file:
        encrypted_file.write(cipher_content)
    print(f"The content in file {file} is now encrypted!")

def decrypted_mode(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()
        print(f"The key {key} is now open")

    cipher_suite = Fernet(key)

    with open(file, "rb") as decrypted_file:
        content = decrypted_file.read()
        cipher_content = cipher_suite.decrypt(content)

    with open(file, "wb") as decrypted_file:
        decrypted_file.write(cipher_content)
    print(f"The content in file {file} is now decrypted!")

parser = argparse.ArgumentParser(description="Crypto program: -f [filename] [key] -m [encrypt] eller [decrypt]")
parser.add_argument("-k", "--key", help="Create a new key")
parser.add_argument("-f", "--files", nargs=2, help="Choose file and key to process")
parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt"], help="Choose an option between [encrypt] and [decrypt] to process")

args = parser.parse_args()

try:
    if args.key:
        if not os.path.exists(args.key):
            generate_key(args.key)
            print("The key is now generated")
        else:
            print("The key already exists")

    elif args.files and args.mode == "encrypt":
        print("Encrypted_mode is activated")
        if os.path.exists(args.files[0]) and os.path.exists(args.files[1]):
            encrypted_mode(args.files[0], args.files[1])
            print("The file is now encrypted")
        else:
            print(f"One or both files {args.files[0]} or {args.files[1]} do not exist")

    elif args.files and args.mode == "decrypt":
        print("Decrypted_mode is now activated")
        if os.path.exists(args.files[0]) and os.path.exists(args.files[1]):
            decrypted_mode(args.files[0], args.files[1])
            print("The file is now decrypted")
        else:
            print(f"One or both files {args.files[0]} or {args.files[1]} do not exist")

except TypeError:
    print("A TypeError occurred")
