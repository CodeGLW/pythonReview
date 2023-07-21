friends = ["Daniel", "Oviya", "Nason", "Caz", "Stephan", "Olivia", "Bianca", "Jen", "Eddie", "Lin", "Teddy", "Shinjoe", "Yiyi", "Marina", "Anika", "Theo", "Bex", "Sam", "Linus", "Neil", "Logan", "Gary", "Nick", "Victor", "Ellise", "Sasha", "Hausen", "Aster"]
print("Here are a bunch of my friends!")
for name in friends:
    print(name)
print("I love " + friends[0] + " and " + friends[1])
print("The last friend on my list is " + friends[-1])
friends[0] = "Cedric"
print("Nevermind! I didn't mean 'Daniel', I meant " + friends[0])
print("The first 5 people I last messaged on Instagram are as follows: " + str(friends[0:5]))
friends.append("Riley")
friends.insert(5, "Charlie")
friends.remove("Charlie")
print("This statement is " + str(("Logan" in friends)) + ": Logan is my friend")
print("Woahhh... I have " + str(len(friends)) + " friends")


friends.clear()
# bye-bye, friends!
