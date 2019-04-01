import random

words = "death"
random_words = random.sample(words, len(words))

jumble = " ".join(random_words)

print(jumble)
loop = True
while loop:
    guess = input("Your answer: ")
    if guess == words:
        print("Yes")
        loop = False
    else:
        print("Try again")
