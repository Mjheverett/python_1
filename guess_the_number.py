import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What's the number? ")) 
    if guess == secret_number:
        print("Yes! You win!")
    elif guess < secret_number:
        print("%d is too low." % guess)
    elif guess > secret_number:
        print("%d is too high." % guess)

playagain = "Y"

while playagain == "Y":
    guess_the_number()
    playagain = input("Would you like to play again? (Y or N)")

print("Bye.")