string = str(input("Give me a string to play with uwu~ "))
print(string)
print(string.upper())
print(string.lower())
eOccurance = int(string.find("e"))
if eOccurance == -1:
    print("There are no lowercase e's in this string")
else:
    print("The first/only time e appears in this string is in index " + str(eOccurance))
    print(string.replace("e", "3"))
secretCode = ('1234' in string)
if secretCode == True:
    print("You found the secret code :)")