from Training import calc

while True:1


    print('kilometers/miles converter. To convert miles, press 1 \nTo convert kilometers press 2.\n To close program press -1:\n')
    try:
        Input_from_user = int(input())
    except ValueError:
        print("please enter valid number\n")
        continue
        
    if Input_from_user == 1:
        miles_from_user = float(input("please enter Miles:"))
        print("Miles: {1:.2f} \nKilo: {0:.2f}".format( calc(miles_from_user).km_calc(),miles_from_user ))

        
    elif Input_from_user == 2:
        Kilo_from_user = float(input("please enter Kilo:"))
        print("Kilo: {1:.2f} \nMiles: {0:.2f}".format( calc(Kilo_from_user).mi_calc(),Kilo_from_user))
        
    elif Input_from_user == -1:
        break
    else:
        print('Please try again\n')

      