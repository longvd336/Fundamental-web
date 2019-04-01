import random

game = ["invoker","jakiro", "techies"]

# word = random.choice(game)
# correct = word
# random_word = random.sample(word, len(word))
# jumble = " ".join(random_word)
print("Welcome to jumble game")
loop = True
while True:
    
    word = random.choice(game)
    correct = word
    random_word = random.sample(word, len(word))
    jumble = " ".join(random_word)
    
    
    print(jumble)
    guess = input("Your answer : ")
                
    if( guess == correct):
                print("yes")
                
                    
    else:
            print("Try again =))")
        





