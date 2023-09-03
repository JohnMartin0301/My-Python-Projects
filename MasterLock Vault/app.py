import os
import time
from cryptography.fernet import Fernet

KEY_FILE = "key.key"
LOCKED_FILES_FILE = "locked_files.txt"

def generate_key():
    return Fernet.generate_key()

def load_key():
    if os.path.isfile(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    else:
        key = generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def lock_file(file_path, key, password):
    encrypt_file(file_path, key)
    with open(LOCKED_FILES_FILE, "a") as locked_file:
        locked_file.write(f"{file_path},{password}\n")

def unlock_file(file_path, key):
    password = input("Enter the password to unlock the file: ")
    with open(LOCKED_FILES_FILE, "r") as locked_file:
        lines = locked_file.readlines()
    for line in lines:
        file_entry = line.strip().split(",")
        if len(file_entry) == 2 and file_entry[0] == file_path and file_entry[1] == password:
            decrypt_file(file_path, key)
            with open(LOCKED_FILES_FILE, "w") as locked_file:
                for updated_line in lines:
                    if updated_line != line:
                        locked_file.write(updated_line)
            print("Unlocking...")
            time.sleep(5)
            print(f"{file_path} is unlocked successfully.")
            return
    print("Unlocking...")
    time.sleep(5)
    print("Incorrect password or file not found.")

def display_locked_files():
    if os.path.isfile(LOCKED_FILES_FILE):
        with open(LOCKED_FILES_FILE, "r") as locked_file:
            lines = locked_file.readlines()
        if lines:
            print("Locked Files:")
            for line in lines:
                file_path, _ = line.strip().split(",")
                print(f"File: {file_path}")
        else:
            print("No locked files.")
    else:
        print("No locked files.")

def main():
    key = load_key()

    while True:
        print("\nWelcome to the MasterLock Vault Program🔒")
        time.sleep(1)
        print("\033[3m'Where your files are kept secretly safe.\033[0m'")
        time.sleep(1.5)
        print("\nOptions:")
        time.sleep(1)
        print("1. MasterLock a File🔐")
        time.sleep(1)
        print("2. Unlock a File🔓")
        time.sleep(1)
        print("3. Display Locked Files📁")
        time.sleep(1)
        print("4. Exit🔚")
        time.sleep(1)
        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the path of the file to lock: ")
            password = input("Enter a password to lock the file: ")
            lock_file(file_path, key, password)
            print("MasterLocking your file...")
            time.sleep(5)
            print(f"{file_path} is MasterLocked successfully.")
        elif choice == "2":
            file_path = input("Enter the path of the file to unlock: ")
            unlock_file(file_path, key)
        elif choice == "3":
            display_locked_files()
        elif choice == "4":
            print("Thank you for using the MasterLock Vault Program.")
            time.sleep(1)
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()