height = float(input("Input your height: "))
credit = int(input("Input your credit: "))

if height >= 5 and credit >= 10:
    print("Enjoy The Ride!")
elif height < 5 and credit >= 10:
    print("You're not tall enough!")
elif height >= 5 and credit < 10:
    print("You don't have enough credits")
else:
    print("You don't meet the requirements")

#what i lerned
# Logical operators and, not, or
# Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not operators:
