import csv
import os
import time

PASSWORDS_FILE = "samplepasswords.csv"

def main():
    if not os.path.isfile(PASSWORDS_FILE):
        create_passwords_file()

    while True:
        print("\nWelcome to PyVault🐍🔒")
        time.sleep(1)
        print("\033[3m'Where your secrets are safe.\033[0m'")
        time.sleep(1.5)
        print("\nPlease choose an option:")
        time.sleep(1)
        print("1. Store Password🔐")
        time.sleep(1)
        print("2. Retrieve Password🔓")
        time.sleep(1)
        print("3. Display Details (Usernames & Passwords)📄")
        time.sleep(1)
        print("4. Exit🔚")
        time.sleep(1)
        choice = input("Enter your choice: ")

        if choice == "1":
            store_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            display_passwords()
        elif choice == "4":
            print("Thank you for using PyVault.")
            time.sleep(1)
            print("Program Terminated.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def create_passwords_file():
    with open(PASSWORDS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Platform", "Username", "Password"])

def store_password():
    platform = input("Enter the name of the platform (Website/APP): ")
    username = input("Enter your username of the platform (Leave empty if none): ")
    password = input("Enter your password: ")

    with open(PASSWORDS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([platform, username, password])
    
    print("Storing your details, please wait...")
    time.sleep(5)
    print(f"Username & Password of {platform} stored successfully✅")

def retrieve_password():
    platform = input("Enter the name of the platform (Website/APP): ")

    with open(PASSWORDS_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == platform:
                username = row[1] if row[1] else "No username"
                print("Retrieving, please wait...")
                time.sleep(5)
                print(f"Platform: {platform}, Username: {username}, Password: {row[2]}")
                return
        print("Retrieving, please wait...")
        time.sleep(5)
        print(f"No stored data found for {platform}.")

def display_passwords():
    with open(PASSWORDS_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            username = row[1] if row[1] else "No username"
            print("Gathering complete details, please wait...")
            time.sleep(5)
            print(f"Platform: {row[0]}, Username: {username}, Password: {row[2]}")

if __name__ == "__main__":
    main()