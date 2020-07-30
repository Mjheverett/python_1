import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What's the number? ")) 
    while guess != secret_number:
        if guess < secret_number:
            print("%d is too low." % guess)
            guess = int(input("What's the number? "))
        elif guess > secret_number:
            print("%d is too high." % guess)
            guess = int(input("What's the number? "))
        print("Yes! You win!")

playagain = "Y"

while playagain == "Y":
    guess_the_number()
    playagain = input("Would you like to play again? (Y or N)")

print("Bye.")