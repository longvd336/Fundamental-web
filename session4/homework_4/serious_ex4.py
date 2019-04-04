total = 0

answer_1 = {
    "1. ": 35,
    "2. ": 36,
    "3. ": 40,
    "4. ": 44 
}

print("Answer the following algebra question :")

print("If x = 8, then what is the value of 4(x +3 ) ?")
for key, value in answer_1.items():
    print(key, value)
 

choice = input("Your choice: ")
if choice == "4":
    print("Huraaaa")
    total += 1
else:
    print(":(")

answer_2 = {
    '1. ' : 'About 55',
    '2. ' : 'About 65',
    '3. ' : 'About 75',
    '4. ' : 'About 85'
}
print('Estimate this answer (exact calculation not needed):')

print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")

for key, value in answer_2.items():
    print(key, value)
 

choice = input("Your choice: ")
if choice == "2":
    print("Huraaaa")
    total += 1   
else:
    print(":(")

print("you correctly answer {} out of 2 questions".format(total))






