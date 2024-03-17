employeeName = input('Enter Employee Name: ')
numShifts = int(input('Enter Number of Shifts Worked: '))
numTransactions = int(input('Enter Number of Transactions: '))
transDollarValue = int(input('Enter Transaction Dollar Value: $'))

employeeBonus = None

prodScore = (transDollarValue / numTransactions) / numShifts


if prodScore <= 30:
    employeeBonus = 50.00

if prodScore >= 31 and prodScore <= 69:
    employeeBonus = 75.00

if prodScore >= 70 and prodScore <= 199:
    employeeBonus = 100.00

if prodScore >= 200:
    employeeBonus = 200.00


print("Employee Name: " + str(employeeName))
print("Employee Bonus: $" + str(employeeBonus))