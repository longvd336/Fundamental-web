n = int(input("Moi nhap so n: "))
tich = 1
if n == 0:
    print(0)
else :
    for i in range(1, n+1):
        tich = tich * i
    print(tich)