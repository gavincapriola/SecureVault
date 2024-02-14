import os
import json
import string
import random
from cryptography.fernet import Fernet

PASSWORDS_FILE = 'passwords.enc'
KEY_FILE = 'secret.key'


def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    return key


def encrypt(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())


def decrypt(token, key):
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()


def save_password(service, username, password, key):
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'rb') as file:
            encrypted_data = file.read()
            data = json.loads(decrypt(encrypted_data, key))
    else:
        data = {}
    data[service] = {'username': username,
                     'password': encrypt(password, key).decode()}
    with open(PASSWORDS_FILE, 'wb') as file:
        file.write(encrypt(json.dumps(data), key))


def get_password(service, key):
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'rb') as file:
            encrypted_data = file.read()
            data = json.loads(decrypt(encrypted_data, key))
        if service in data:
            username = data[service]['username']
            password = decrypt(data[service]['password'].encode(), key)
            return username, password
    return None, None


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def main():
    key = load_or_create_key()
    while True:
        print("\nPassword Manager")
        print("1. Generate and save a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            service = input("Service name: ")
            username = input("Username: ")
            password = generate_password()
            save_password(service, username, password, key)
            print(f"Password for {service} saved.")
        elif choice == '2':
            service = input("Service name: ")
            username, password = get_password(service, key)
            if username:
                print(f"Username: {username}, Password: {password}")
            else:
                print("Service not found.")
        elif choice == '3':
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
