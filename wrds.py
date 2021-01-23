from random import randint

with open("banned_words.txt", "r") as f:
    words = f.read()
    check_word = input("Check word: ")
    if check_word not in words:
        print(check_word)
    else:
        print("*" * randint(1, 15))
