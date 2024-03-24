import random


def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)


def get_valid_number():
    """Prompts the user for a number and checks its validity."""
    while True:
        num = input('Enter a number from 1 to 100: ')
        if num.isdigit() and 0 < int(num) < 101:
            return int(num)
        print('Please enter a valid number between 1 and 100.')


def main():
    target_number = generate_random_number()
    print('Welcome to the Number Guessing Game!')

    while True:
        guessed_number = get_valid_number()
        if guessed_number < target_number:
            print(f'The target number is greater than {guessed_number}. Try again.')
        elif guessed_number > target_number:
            print(f'The target number is less than {guessed_number}. Try again.')
        else:
            print(f'Congratulations! You guessed the number {target_number}.')
            break


if __name__ == "__main__":
    main()
