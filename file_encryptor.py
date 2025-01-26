# File Encryptor Script
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, encrypted_path):
    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(encrypted_path.replace('.enc', ''), 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    key = generate_key()
    print(f"Generated Key: {key.decode()}")
    file_path = input("Enter the file path to encrypt: ")
    encrypt_file(key, file_path)
    print("File encrypted successfully.")