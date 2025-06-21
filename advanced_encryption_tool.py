from cryptography.fernet import Fernet
import os

KEY_FILE = 'encryption.key'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            return key_file.read()
    else:
        return generate_key()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename + '.enc', 'wb') as enc_file:
        enc_file.write(encrypted)
    print(f"✅ Encrypted file saved as: {filename}.enc")

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    decrypted_filename = filename.replace('.enc', '_decrypted')
    with open(decrypted_filename, 'wb') as dec_file:
        dec_file.write(decrypted)
    print(f"✅ Decrypted file saved as: {decrypted_filename}")

def main():
    print("🔐 Advanced Encryption Tool")
    print("===========================")
    key = load_key()

    choice = input("Do you want to (e)ncrypt or (d)ecrypt a file? [e/d]: ").lower()
    if choice not in ('e', 'd'):
        print("❌ Invalid choice.")
        return

    filename = input("Enter the full path of the file: ")

    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    if choice == 'e':
        encrypt_file(filename, key)
    elif choice == 'd':
        decrypt_file(filename, key)

if __name__ == '__main__':
    main()
