sheepSize = [5,11,100,20,30,50,60]

define_size = 8

loop = True
count = 1
print( "Hello , my name is Long and these are my shep sizes")
print()
print(sheepSize)

bigest = int(max(sheepSize))   #tim phan tu lon nhat trong list

print("Now my bigest sheep hax size" , bigest , "let's shear it" )
print("After shearing , here is my flock")


index = sheepSize.index(bigest)    #thay gia tri lon nhat bang gia tri define = 8 

sheepSize[index] = define_size

print(sheepSize)
print()

#nhap so thang muon tinh de mac dih la 4 thang  
#  co the lam nhap tu ban phim dc :v 
 
month = 4


while loop:
    
    if( count < month):
        
        print ("MONTH", count )
        #tang gia tri sau moi thang
        print("One month passed , now these are my flock")

        for i in range(len(sheepSize)):         
            sheepSize[i]+=50

        print(sheepSize)
        
        
        #dat lai gia tri lon nhat cua list

        bigest = int(max(sheepSize))

        print("Now my bigest sheep hax size" , bigest , "let's shear it" )
           
        print("After shearing , here is my flock")            
        index = sheepSize.index(bigest)

        sheepSize[index] = define_size

        print(sheepSize)

        print()
        count+=1
    else:
        
        print( "MONTH", month)
        print("One month passed , now these are my flock")
        
        for i in range(len(sheepSize)):
            sheepSize[i]+=50

        print(sheepSize)
        print()
        print("My flock has size in total :", end = " ")
        total = 0
        
        #tinh tien 
        for i in range(len(sheepSize)):
            total = total + sheepSize[i]
        
        print(total)
        money = total * 2
        print (" I would get" , total , "* 2$ = ", money , "$" )
        loop = False








