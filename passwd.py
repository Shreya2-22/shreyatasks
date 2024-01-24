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

def change_password(username, current_password, new_password, password_file="passwd.txt"):
    encrypted_current_password = rot13(current_password)
    encrypted_new_password = rot13(new_password)

    with open(password_file, "r") as file:
        lines = file.readlines()

    with open(password_file, "w") as file:
        password_changed = False
        for line in lines:
            parts = line.split(":")
            stored_username = parts[0].strip()
            stored_password = parts[2].strip()
            if stored_username == username and stored_password == encrypted_current_password:
                file.write(f"{parts[0]}:{parts[1]}:{encrypted_new_password}\n")
                password_changed = True
            else:
                file.write(line)

        if password_changed:
            print("Password changed.")
        else:
            print("Current password is invalid.")

if __name__ == "__main__":
    username = input("User: ")
    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match.")

