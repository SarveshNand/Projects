import random
low = 1
high = 100
counter = 0

print("Think of a number between 1 and 100")

while True:
    computer = random.randint(low, high)
    counter += 1
    print(f"Computer guesses: {computer}")
    feedback = input("Is it too high (h), too low (l), or correct (c)? ")
    if feedback == 'h':
        print("Too high!")
        high = computer - 1
    elif feedback == 'l':
        print("Too low!")
        low = computer + 1
    elif feedback == 'c':
        print("============================================================================")
        print(f"Computer got the correct guess in {counter} guesses, which is {computer}")
        print("============================================================================")
        break