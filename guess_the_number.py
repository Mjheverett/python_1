import random
playagain = "Y"
while playagain == "Y":
    secret_number = random.randint(1, 10)
    guessesleft = 5
    print("I am thinking of a number between 1 and 10.")
    print("You have %d guesses left." % guessesleft)
    guess = int(input("What's the number? "))
    while (guessesleft > 0) & (guess != secret_number):
        if guessesleft == 0:
            print("You have no guesses left.")
        else:
            if guess == secret_number:
                print("Yes! You win!")
            elif guess < secret_number:
                print("%d is too low." % guess)
                guessesleft -= 1
            elif guess > secret_number:
                print("%d is too high." % guess)
                guessesleft -= 1
        print("You have %d guesses left." % guessesleft)
        guess = int(input("What's the number? "))
        
    playagain = input("Would you like to play again? (Y or N)")
print("Bye.")