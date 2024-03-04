minYear = 0
minMonth = 1
maxMonth = 12
minDay = 1
maxDay = 31
validDate = True

year = input('Enter Year')
day = input('Enter Day')
month = input('Enter Month') 


if year < minYear:
    validDate = False 
elif year > minYear:
    validDate = True 
elif year < minMonth:
    validDate = False
elif month >= minMonth:
    validDate = True
elif month > maxMonth:
    validDate = False
elif month <= maxMonth:
    validDate = True
elif day < minDay:
    validDate = False
elif day >= minDay:
    validDate = True
elif day > maxDay:
    validDate = False
elif day <= maxDay:
    validDate = True


if validDate == True:
    print(str(month) + '/' +str(day) + '/' + str(year) + 'is a valid date')
if validDate == False:
    print(str(month) + '/' +str(day) + '/' + str(year) + 'is not a valid date')