# teenCode = {
#     "hc":"hoc :v",
#     "ck":"chong ",
#     "vk":"vo",
#     "ik": "di",
# }
# print("you want to search? ")

# word = input()

# print(teenCode[word])

teenCode = {
     "hc":"hoc :v",
     "ck":"chong ",
     "vk":"vo",
     "ik": "di",
 }

loop = True
while loop:
    print("you want to search? ")

    word = input()

    if word in teenCode:
        print(teenCode[word])
    else :
        print("Khong co trong tu dien")
        answer = input("you want to update my dict? press Y/N ").upper()

        if (answer == "Y"):
            your_word = input("Your word: ")
            
            meaning = input("y nghia cua no la gi ?")
            
            teenCode[your_word] = meaning
            
            print(*teenCode, sep  =" ")

        else :
            print("Thank you~~")
            loop = False
       






