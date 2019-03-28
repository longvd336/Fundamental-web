n = int(input("nhap so n: "))

for i in range(n):
    if( i%2==0 ):
        print("x", end=" ")
    else:
        print("*", end=" ")