width = int(input("Width? "))
height = int(input("Height? "))

for y in range (1, height + 1):
    if y == 1 or y == height:
        print("*" * width)
    elif 1 < y < height:
        print("*" + (" " * (width - 2)) + "*")