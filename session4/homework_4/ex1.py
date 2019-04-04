x = input("String : ")

x = x.lower()   

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

letter_counts = {} 

for char in x:
    if char in alphabet: 
        if char in letter_count:
            letter_counts[char] = letter_counts[char] + 1
        else:
            letter_counts[char] = 1

keys = letter_counts.keys()
for char in sorted(keys):
    print(char, letter_counts[char])