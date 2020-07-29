import random
playagain = "Y"
while playagain == "Y":
    secret_number = random.randint(1, 10)
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What's the number? ")) 
    if guess == secret_number:
        print("Yes! You win!")
    elif guess < secret_number:
        print("%d is too low." % guess)
        guessesleft -= 1
    elif guess > secret_number:
        print("%d is too high." % guess)
        guessesleft -= 1    
    else:
        print("You have no guesses left." % guessesleft)
        

    playagain = input("Would you like to play again? (Y or N)")
print("Bye.")