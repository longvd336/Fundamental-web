#List
#cu phap var = [...]
#Index 

# print(menu)
# print(menu[2])

#duyet tung ptu
#sd loop:
#loop items

# for item in menu:
#     print(item)

#loop index
# len
# for index in range(len(menu)):
#     print(index)


#loop item and index
# for index, item in enumerate(menu):
#     print(index, item )


#2. CREATE
#them
# menu = ["com", "canh", "thit"]
# n = input()
# menu.append(n)
# print(menu)

sothich =[" game ", "bong da", "ngu ","hoc", "choi"]
print(*sothich, sep=",")
a = input()
sothich.append(a)
print(*sothich, sep=",")

#SEP="KI TU"

# print("Hi there you favorite things so far")
# sothich =[" game ", "bong da", "ngu ","hoc", "choi"]
#sd enumerate
# for index,item in enumerate(sothich):
    # print(index +1 , item, sep=". ")

#sd format
    # print("{}. {}".format(index+1,item))

#3. UPDATE:
# sothich =[" game ", "bong da", "ngu ","hoc", "choi"]

# sothich[0] = "vatly"
# print(sothich)

#4.DELETE
#cach 1 : delete theo index
# sothich =[" game ", "bong da", "ngu ","hoc", "choi"]

# del sothich[1]
# print(sothich)
#cach 2: delete 

# sothich =[" game ", "bong da", "ngu ","hoc", "choi"]
# sothich.remove(" game ")
# print(sothich)



