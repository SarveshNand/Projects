import random
computer = random.randint(1, 100)
counter = 0

print("Guess of a number from 1 and 100")

while True:
    user = int(input("Your guess: "))
    if computer > user:
        print("Too low!")
    elif computer < user:
        print("Too high!")
    elif computer == user:
        print(f"Congratulations!, you got the correct guess which is {user}")
        print(f"Got the correct guess in {counter + 1} guesses.")
        break
    counter += 1