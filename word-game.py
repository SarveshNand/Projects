import random
fruits = ['orange', 'apple', 'mango', 'banana', 'kiwi', 'strawberry', 'lemon', 'avacado', 'apricot', 'cherry', 'coconut', 'papaya', 'date', 'guava', 'blueberry', 'lime', 'peach', 'pear', 'watermelon', 'pomegranate', 'rasberry', 'plum', 'pineapple', 'grape', 'grapefruit', 'cranberry', 'fig', 'dragonfruit', 'tamarind', 'jackfruit', 'nectarine', 'raisin']

while True:

    computer = random.choice(fruits)
    hint = len(computer)
    print(f'The fruit is of length: {hint}')
    lives = 10

    while lives > 0:
        user = input('Enter your guess: ').lower()
        if user == computer:
            print(f'You won with your {lives} lives')
            break
        else:
            lives -= 1
            print(f'You guessed wrong! -> Remaining lives: {lives}')

        if lives == 0:
            print(f'The correct guess -> {computer}')
            print(f'You lost completely with your remaining {lives} lives')
            break

    resume = input('Wanna play again? (y or n): ').lower()

    if resume == 'y':
        continue
    elif resume == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice! Now, play again :)')