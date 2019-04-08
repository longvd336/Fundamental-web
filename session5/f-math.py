from random import*
import calculate

loop = True
while loop :
    x = randint(0,9)
    y = randint(0,9)

    op = choice(["+", "-", "*", "/"])
    
    result = calculate.tinhToan( x , y, op )
    
    # result = 0
    # if op == "+":
    #     result = x + y

    # if op == "-":
    #     result = x - y

    # if op == "*":
    #     result = x * y

    # if op =="/":
    #     result = x / y
    
    
    fake = randint(result-2 , result + 2 )
    
    print("{} {} {} = {}".format(x , op , y , fake ))

    answer = input("Y/N ? ").lower()

    if fake == result:
        if(answer == "y"):
            print("yes")
        else:
            print(" :( ")

    if fake != result:
        if(answer == "n"):
            print("Yes")
        else:
            print(":(")




