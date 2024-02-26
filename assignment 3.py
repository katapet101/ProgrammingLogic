retailPrice = 325.0
wholesalePrice = 200.0
profit = retailPrice-wholesalePrice
salePrice = retailPrice-(retailPrice*0.25)
saleProfit = salePrice-wholesalePrice

print("Item Name: TV Stand")
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))