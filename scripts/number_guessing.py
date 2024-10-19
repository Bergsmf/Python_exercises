from random import randint

def choose_number_range() -> int:
    print('By choosing a number, the raffle will be between 1 and the chosen number.')
    max_number = int(input('Select the maximum number for the raffle: '))
    raffled_number = randint(1, max_number)
    return max_number, raffled_number

def guess_number(max_number: int, raffled_number: int) -> bool:
    user_guess = int(input(f'Guess a number between 1 and {max_number}: '))
    if user_guess == raffled_number:
        return True
    elif user_guess > raffled_number:
        print('Your guess is higher than the raffled number.')
        return False
    else:
        print('Your guess is lower than the raffled number.')
        return False

def main():
    max_number, raffled_number = choose_number_range()
    is_correct_guess = False
    attempts = 0
    while not is_correct_guess:
        is_correct_guess = guess_number(max_number, raffled_number)
        attempts += 1
    print(f'Congratulations! You guessed the number in {attempts} attempts.')

if __name__ == '__main__':
    main()