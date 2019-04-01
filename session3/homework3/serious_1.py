
items = ["T - shirt" , " Sweater"]

loop = True

while loop:
    print("Welcome to our shop , what do you want ( C, R, U , D )?")
    n = input() 
    
    if n.upper() == "R":

        print("Our items:", end = " " )
        print(* items, sep ="," )
        

    elif n.upper() == "C":
        print("enter item: ")
        nhap = input()
        
        items.append(nhap)

        print("our items: ", end = " ")
        print(* items, sep = "," ) 
        
        
    elif n.upper() == "U":
        print("Update position? ")
        a = int(input())
        if a> len(items):
            print("out off range")
            
        else:
            print("new item ?")
            new = input()

            items[a-1] = new
            print("our items: ", end = " ")
            print(* items, sep = "," ) 
    elif n.upper() == "D":
        print("Delete position? ")
        xoa = int(input())
        if xoa > len(items):
            print("out of range")
                   
        else :
            del items[xoa-1]
            print("our items: ", end = " ")
            print(* items, sep = "," ) 

        
        
        



