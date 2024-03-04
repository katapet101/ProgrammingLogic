minYear = 0
minMonth = 1
maxMonth = 12
minDay = 1
maxDay = 31
validDate = True


month = input('Enter Month: ') 
day = input('Enter Day: ')
year = input('Enter Year: ')


if int(year) < minYear:
    validDate = False
elif int(month) < minMonth or int(month) > maxMonth:
    validDate = False
elif int(day) < minDay or int(day) > maxDay:
    validDate = False


if validDate == True:
    print(str(month) + '/' +str(day) + '/' + str(year) + ' is a valid date')
if validDate == False:
    print(str(month) + '/' +str(day) + '/' + str(year) + ' is not a valid date')
