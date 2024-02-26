salary = 1250.0
numDependents = 2
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = numDependents * (salary * 0.025)
totalWitholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWitholding

print("State Tax: " + str(stateTax))
print("Federal Tax: " + str(federalTax))
print("Dependents: " + str(dependentDeduction))
print("Salary: " + str(salary))
print("Take-Home Pay: " + str(takeHomePay))