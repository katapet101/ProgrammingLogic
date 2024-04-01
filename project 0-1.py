AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']



print('*******************************')

print('AutoCountry Vehicle Finder v0.1')

print('*******************************')

print('Please Enter the following number below from the following menu:')

print('')

print('1. PRINT all Authorized Vehicles')

print('2. Exit')

query = input()

if int(query) == 1:
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for AllowedVerhicles in AllowedVehiclesList:
        print(AllowedVerhicles)
else:
    print('Thank you for using the AutoCounty Vehicle Finder, good-bye!')