from cryptography.fernet import Fernet  # type: ignore
import json
import os


class PasswordManager:
    def __init__(self):
        self.DATA_FILE = "data/passwords.json"
        self.KEY_FILE = "data/secret.key"
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Ensure the data directory exists"""
        os.makedirs(os.path.dirname(self.DATA_FILE), exist_ok=True)

    def load_key(self):
        if not os.path.exists(self.KEY_FILE):
            key = Fernet.generate_key()
            with open(self.KEY_FILE, "wb") as key_file:
                key_file.write(key)
        else:
            with open(self.KEY_FILE, "rb") as key_file:
                key = key_file.read()
        return key

    def encrypt_password(self, password, key):
        cipher = Fernet(key)
        return cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password, key):
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_password.encode()).decode()

    def save_password(self, service, username, password):
        key = self.load_key()
        encrypted_password = self.encrypt_password(password, key)
        data = {}

        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

        data[service] = {"username": username, "password": encrypted_password}

        with open(self.DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def retrieve_password(self, service):
        key = self.load_key()
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)
                if service in data:
                    username = data[service]["username"]
                    encrypted_password = data[service]["password"]
                    password = self.decrypt_password(encrypted_password, key)
                    return username, password
        return None, None
