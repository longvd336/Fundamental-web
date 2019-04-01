n = int(input())

count = 0
a = True
while a:
    for i in range(1,n):
        if(n % i==0):
            count +=1
            a = False
print(count)
if(count != 1):
    print("ko la snt")
else:
    print("la so nguyen to")



#cach2: