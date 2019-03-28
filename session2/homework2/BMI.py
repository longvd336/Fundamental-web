weight = int(input("Moi nhap can nang: "))
height = int(input("Moi nhap chieu cao(cm): "))

conversion = height/100

bmi = weight/(conversion**2)
if bmi < 16:
    print( "Severely underweight")
elif bmi < 18.5:
    print( "Underweight" )
elif bmi < 25:
    print( "Normal")
elif bmi < 30:
    print( "Overweight")
else:
    print( "Obese")
