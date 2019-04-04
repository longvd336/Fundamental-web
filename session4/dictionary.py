#cu phap : var = {key : value,}
person = {
    "Name: " :"Duc ",
    "age: ": 22,
    "school: " : "FTU",
    "gf:": "3", 
}

# I-Read : 

# print( person )

# print(person["Name "])
# print(person["age "])

# 1-loop by key:

# for key in person.keys():
#     print(key)

# 2-loop by value

# for value in person.values():
#     print(value)

#3- loop by item:

# for key,value in person.items():
#     print(key, value)

# II-creat and update:

person[" gender "] = " male "
print(person)

# update:

person["gf:"] = 6
print(person)
print()
# DELETE :

del person["age: "]
print(person)

# sd list khi cac phan tu chua trong list co cung tih chat


