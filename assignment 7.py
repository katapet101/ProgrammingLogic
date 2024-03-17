charge = 0.00
numChars = 18
color = "black"
woodType = "oak"

charge = 35.00

if numChars > 5:
    charge += 4 * (numChars - 5)

if woodType == "oak":
    charge += 20.00

if color == "gold":
    charge += 15.00


print("The charge for this sign is $" + str(charge))