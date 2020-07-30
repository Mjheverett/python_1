import random

def guess_the_number(secret_number):
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What's the number? ")) 
    number_of_guess = 5
    guesses_made = 0
    while guess != secret_number and (number_of_guess - 1) != guesses_made:
        if guess < secret_number:
            print("%d is too low." % guess)
            guesses_made += 1
        elif guess > secret_number:
            print("%d is too high." % guess)
            guesses_made += 1
        print("You have %d guesses left." % (number_of_guess - guesses_made))
        guess = int(input("What's the number? "))    
    if (number_of_guess - 1) == guesses_made:
        print("You ran out of guesses.")
    else:
        print("Yes! You win!")

playagain = "Y"

while playagain == "Y":
    secret_number = random.randint(1, 10)
    guess_the_number(secret_number)
    playagain = input("Would you like to play again? (Y or N)").upper()
    
print("Bye.")