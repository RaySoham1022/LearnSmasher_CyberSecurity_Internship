import re
import string

def entropycalculator(password):

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    numbers = "0123456789"
    special_chars = string.punctuation

    charsets = [lowercase, uppercase, numbers, special_chars]
    entropy = sum(len(charset) for charset in charsets if any(char in password for char in charset))

    entropy *= len(password)

    return entropy

def passwordweak(password):

    weak_patterns = [
        r"\b123456\b",
        r"\bqwerty\b",
    ]
    with open('weak_passwords.txt', 'r') as file:
        weak_passwords = {line.strip() for line in file}

    if any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
        return True

    if password.lower() in weak_passwords:
        return True

    if password.isalpha():
        return True

    if password.isnumeric():
        return True

    return False

def strongpasswordchecker(password):

    length = len(password)
    entropy = entropycalculator(password)

    if passwordweak(password):
        return "\nYour Password is WEAK !! You should avoid using it !! \n"

    if length >= 8 and length < 12:
        if (any(char.islower() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.islower() for char in password) and any(char.isupper() for char in password)) or \
           (any(char.islower() for char in password) and any(char in string.punctuation for char in password)) or \
           (any(char.isupper() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.isupper() for char in password) and any(char in string.punctuation for char in password)):
            return "\nYour Password Strength is MODERATE !! Increase Complexity for Better Security !!\n"

    if length >= 12 and entropy >= 60:
        return "\nYour Password is STRONG !! Congratulations !! \n"

    return "\nYour Password is WEAK !! You should avoid using it !!\n"

def getpass():

    # import getpass
    # password = getpass.getpass("Enter your password: ")

    password = input("\nEnter Your Password :  ")
    return password

def main():
    password = getpass()
    strength = strongpasswordchecker(password)
    print(strength)

if __name__ == "__main__":
    main()