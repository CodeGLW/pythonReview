birthYear = input("What year were you born (yyyy please)? ")
age = 2023 - int(birthYear)

print("If you've had you're birthday this year already, you're " + str(age) + " years old.")
print("If not, you're", str(age-1), "years old")