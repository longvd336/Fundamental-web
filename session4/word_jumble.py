from random import choice
word = "champion"

word_list = list(word)
print(word_list)

shuffle_word = []
for i in range(len(word)):

    character = choice(word_list)
    shuffle_word.append(character)
    word_list.remove(character)


print(*shuffle_word, sep=" ")
input_answer = input("your answer: ")
if input_answer == word:
    print("yes")
else :
    print("wrong")


