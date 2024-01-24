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

def check_existing_username(username):
    with open('passwd.txt', 'r') as f:
        lines = f.readlines()
        existing_usernames = [line.split(':')[0] for line in lines]
        return username in existing_usernames

def add_user(username, real_name, password):
    if check_existing_username(username):
        print("Cannot add. Most likely username already exists.")
    else:
        encrypted_password = rot13(password)
        with open('passwd.txt', 'a') as f:
            f.write(f"{username}:{real_name}:{encrypted_password}\n")
        print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")
    
    add_user(username, real_name, password)