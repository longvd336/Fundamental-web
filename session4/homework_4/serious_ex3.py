answer = {
    "1. ": 35,
    "2. ": 36,
    "3. ": 40,
    "4. ": 44 
}


print("Answer the following algebra question :")

print("If x = 8, then what is the value of 4(x +3 ) ?")
for key, value in answer.items():
    print(key, value)
 
loop = True
while loop:
    choice = input("Your choice: ")
    if choice == "4":
        print("Huraaaa")
        loop = False
    else:
        print(":(")
        


