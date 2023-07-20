weight = float(input("Please enter your weight "))
unit = input("Are you using kilograms (k) or pounds (l)? ")
if unit == ("L") or unit == ("l"):
    newWeight = weight/2.2
    newWeight = format(newWeight, '.2f')
    unit = ("kilograms")
elif unit == ("K") or unit == ("k"):
    newWeight = weight*2.2
    newWeight = format(newWeight, '.2f')
    unit = ("pounds")

print("Your converted weight is " + str(newWeight) + " " + str(unit) + ".")