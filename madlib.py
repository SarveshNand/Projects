resume = input('Want to start the game? (y or n): ').lower()
while resume == 'y':
    name = input("What's your name: ")
    noun1 = input("Enter a plural noun: ")
    noun2 = input("Enter any noun: ")
    adjective = input("Enter an adjective: ")

    # Print Rhyme
    print('========================================================================================')
    print(f"After hiding the painting in his {noun1} for two\nyears, he grew {adjective} and tried to sell it\nto a/an {noun2} in Florence, but was caught.")
    print(f"\t\t\t\t~By {name}")
    print('========================================================================================')
    resume = input("Want to do again?(y or n): ").lower()
print("Thanks for playing!")