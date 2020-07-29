initialnum = int(input("Give me a number to factor: " ))
for x in range (1, initialnum):
    if (initialnum % x) == 0:
        print(x)
print(initialnum)