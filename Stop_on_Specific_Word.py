while True:
    word = input("Type a word: ")
    if word.lower() == "stop":
        print("Program stopped.")
        break
    print("You typed:", word)
