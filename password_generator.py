import random
import string

# Function to prompt user preferences for password characters
def acceptable_chars():
    chars = ''
    while True:
        pwd_digits = input('Include digits 0 to 9 in the password? ').lower()
        if pwd_digits in ['yes']:
            chars += string.digits
            break
        elif pwd_digits in ['no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        pwd_uppercase = input('Include uppercase letters in the password? ').lower()
        if pwd_uppercase in ['yes']:
            chars += string.ascii_uppercase
            break
        elif pwd_uppercase in ['no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        pwd_lowercase = input('Include lowercase letters in the password? ').lower()
        if pwd_lowercase in ['yes']:
            chars += string.ascii_lowercase
            break
        elif pwd_lowercase in ['no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        pwd_punctuation = input('Include symbols "!#$%&*+-=?@^_" in the password? ').lower()
        if pwd_punctuation in ['yes']:
            chars += '!#$%&*+-=?@^_'
            break
        elif pwd_punctuation in ['no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")

    while True:
        pwd_exceptions = input('Exclude ambiguous characters "il1Lo0O" from the password? ').lower()
        if pwd_exceptions in ['yes']:
            chars = ''.join(char for char in chars if char not in 'il1Lo0O')
            break
        elif pwd_exceptions in ['no']:
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    return chars

# Function to generate a password of specified length
def generate_password(pwd_len, chars):
    return ''.join(random.choices(chars, k=pwd_len))

def main():
    pwd_quantity = int(input('How many passwords do you need to generate? '))
    pwd_len = int(input('What length should the password be? '))
    for _ in range(pwd_quantity):
        chars = acceptable_chars()
        password = generate_password(pwd_len, chars)
        print(password)

if __name__ == '__main__':
    main()
