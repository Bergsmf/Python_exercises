from string import digits
from random import choice


def generate_number() -> str:
    numbers = str(digits)
    number = ''
    for _ in range(0, 5):
        drawn = choice(numbers)
        number = number + drawn
        numbers = numbers.replace(drawn, '')
    return number


def request_guess() -> str:
    is_valid = False
    while not is_valid:
        guess = input('Enter your guess (must be 5 distinct digits):\n')
        if (guess.isdigit() and
            len(set(guess)) == 5 and
            len(guess) == 5):
            is_valid = True
        else:
            print('Invalid input! Please enter exactly 5 distinct digits (e.g., 12345).')
    return guess


def check_guess(number: str, guess: str) -> str:
    comparison = ''
    for i in range(0, 5):
        if(number[i] == guess[i]):
            comparison = comparison + '.'
        elif(guess[i] in number):
            comparison = comparison + '-'
        else:
            comparison = comparison + '_'
    print(comparison)
    return comparison


def main():
    explanation = '''Guess the number rules:
    1. A 5-digit number, without repetition, is drawn.
       Your goal is to figure it out;
    2. Enter your guess and a response will be shown.
       According to the position of each digit in your guess,
       the feedback will be:
       . > For a digit in the correct position;
       - > For a correct digit, but in the wrong position;
       _ > For an incorrect digit
    3. Repeat the process until you guess the number;
    Good luck!'''
    print(explanation)
    number = generate_number()
    result = ' ' * 5
    attempt = 0
    while result != '.' * 5:
        guess = request_guess()
        result = check_guess(number, guess)
        attempt += 1
    print(f'Congratulations, you guessed it on attempt {attempt}')


if __name__ == '__main__':
    main()