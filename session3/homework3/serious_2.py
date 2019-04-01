sheepSize = [5,11,100,20,30,50,60]

define_size = 8

loop = True
count = 1
print( "Hello , my name is Long and these are my shep sizes")
print()
print(sheepSize)
bigest = int(max(sheepSize))

print("Now my bigest sheep hax size" , bigest , "let's shear it" )
print("After shearing , here is my flock")

index = sheepSize.index(bigest)

sheepSize[index] = define_size

print(sheepSize)
print()

month = input()
while loop:
    
    if( count < int(month)):
        
        print ("MONTH", count )
        
        print("One month passed , now these are my flock")
        
        for i in range(len(sheepSize)):
            sheepSize[i]+=50

        print(sheepSize)
        
        
        
        bigest = int(max(sheepSize))

        print("Now my bigest sheep hax size" , bigest , "let's shear it" )
            
        print("After shearing , here is my flock")

        index = sheepSize.index(bigest)

        sheepSize[index] = define_size

        print(sheepSize)

        print()
        count+=1
    else:
        print("One month passed , now these are my flock")
        
        for i in range(len(sheepSize)):
            sheepSize[i]+=50

        print(sheepSize)
        print()
        print("My flock has size in total :", end = " ")
        total = 0
        for i in range(len(sheepSize)):
            total = total + sheepSize[i]
        
        print(total)
        money = total * 2
        print (" I would get" , total , "* 2$ = ", money , "$" )
        loop = False








