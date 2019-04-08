x = int(input("x:"))
y = int(input("y:"))

pheptinh = input("phep tinh")


result = 0

if pheptinh == "+":
    result = x + y

if pheptinh == "-":
    result = x - y

if pheptinh == "*":
    result = x * y

if pheptinh =="/":
    result = x / y

print("{0} {1} {2} = {3}".format(x, pheptinh, y, result))

