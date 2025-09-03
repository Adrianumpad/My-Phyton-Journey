import random

question = input("What is you question?: ")

answer = [
    "Yes - definitely.", 
    "It is decidedly so.", 
    "without a doudt", 
    "reply hazy, try again", 
    "ask again later", 
    "better not tell you now", 
    "My source say no",
    "outlook not so good", 
    "very doubtful"
]

answer = random.choice(answer)
print(answer)

# what i learned
#random.choice() → use it to pick a random item from a list.
#randint() → only works for numbers, not strings.
#Strings must be stored in a list [...] if you want to choose from them.
