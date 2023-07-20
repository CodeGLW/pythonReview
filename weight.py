weight = float(input("Please enter your weight "))
unit = input("Are you using kilograms (K) or pounds (L)? ")
if unit.upper() == ("L"):
    newWeight = weight/2.2
    newWeight = format(newWeight, '.2f')
    print("Your converted weight is " + newWeight + " kilograms.") 
else:
    newWeight = weight*2.2
    newWeight = format(newWeight, '.2f')
    print("Your converted weight is " + newWeight + "pounds.")
