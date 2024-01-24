import getpass

def rot13(text):
    encrypting = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            encrypting += chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            encrypting += char
    return encrypting

def login(username, password, password_file="passwd.txt"):
    encrypted_password = rot13(password)
    with open(password_file, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == username and parts[2].strip() == encrypted_password:
                print("Access granted.")
                return
        print("Access denied.")

if __name__ == "__main__":
    username = input("User: ")
    password = getpass.getpass("Password: ")
    login(username, password)
