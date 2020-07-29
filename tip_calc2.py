bill = float(input("Total bill amount? "))
service = input("Level of service? ")
split = int(input("Split how many ways? "))
if service == "good":
    tipperc = 0.2
elif service == "fair":
    tipperc = 0.15
elif service == "bad":
    tipperc = 0.1
else:
    print("Please enter: good, fair, or bad")
tip = bill * tipperc
total = bill + tip
ampp = total / split
print("Tip amount: %.2f" % tip)
print("Total amount: %.2f" % total)
print("Amount per person: %.2f" % ampp)