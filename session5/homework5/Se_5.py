def is_inside(l,i):
    if(i[0] < l[0] <i[0]+i[2] and i[1]< l[1]< i[1]+i[3]):
        print(True)
        
    else:
        print(False)

is_inside([200,120], [140,60,100,200])


