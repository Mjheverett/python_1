title = "Electric Boogaloo"
# STOP = 10
counter = 0

while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter += 1