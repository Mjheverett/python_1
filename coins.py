coins = 0
print("You have %d coins." % coins)
morecoin = input("Would you like another? ")
while morecoin == "yes":
    coins += 1
    print("You have %d coins." % coins)
    morecoin = input("Would you like another? ")
print("Bye.")