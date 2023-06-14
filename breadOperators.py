budget = int(input("Hello! I'm Brad, the bread baker of this fine town. Tell me your budget and I'll tell you what you can buy. "))
if budget <= (4):
    print ("I'm sorry boy'o, but you don't seem to have enough for my bread shop. Come back later!")
elif budget >= (5) and budget <= (100):
    loaves = budget//5
    print("How rad! You have enough for " + str(loaves) + " loaves!")
elif not budget < (101):
    print("Oh goody good good! You are mighty rich, aren't ya. Take my entire store!!! <3")