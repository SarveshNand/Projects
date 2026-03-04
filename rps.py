import random
counter = 0
computer_counter = 0
user_counter = 0

while True: 
    computer = random.choice(['rock', 'paper', 'scissors'])
    user = input("Pick from rock, paper or scissors: ").lower()
    counter += 1
    if user == computer:
        print("Tied")

    elif user == 'rock' and computer == 'paper':
        print("Computer Won!")
        computer_counter += 1
    elif user == 'rock' and computer == 'scissors':
        print("You Won!")
        user_counter += 1

    elif user == 'paper' and computer == 'rock':
        print("You Won!")
        user_counter += 1
    elif user == 'paper' and computer == 'scissors':
        print("Computer Won!")
        computer_counter += 1

    elif user == 'scissors' and computer == 'rock':
        print("Computer Won!")
        computer_counter += 1
    elif user == 'scissors' and computer == 'paper':
        print("You Won!")
        user_counter += 1
    
    else:
        print("Invalid Choice! Please pick rock, paper, or scissors.")
        continue

    print(f"Score -> You: {user_counter}, Computer: {computer_counter}, Ties: {counter - user_counter - computer_counter}")

    ask = input('Want to play another game? (y or n): ')
    if ask == 'y':
        continue
    elif ask == 'n':
        print("Thank you for playing this game :)")
        break
    else:
        print("Invalid Choice! Now, Play again.")

print("==========================================================================================")
print(f"The game score in {counter} rounds ->\nYours: {user_counter} Computer: {computer_counter} Tie: {counter - (user_counter + computer_counter)}")
print("==========================================================================================")