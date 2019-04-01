sheepSize = [5,11,100,20,30,50,60]
define_size = 8
print( "Hello , my name is Long and these are my shep sizes")
print()
print(sheepSize)

bigest = int(max(sheepSize))   #tim phan tu lon nhat trong list

print("Now my bigest sheep hax size" , bigest , "let's shear it" )


print("After shearing , here is my flock")


index = sheepSize.index(bigest)    #thay gia tri lon nhat bang gia tri define = 8 

sheepSize[index] = define_size

print(sheepSize)


print("One month passed , now these are my flock")

for i in range(len(sheepSize)):         
    sheepSize[i]+=50

print(sheepSize)