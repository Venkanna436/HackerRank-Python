import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

if D > 0:
    print("Two distinct real roots")
    print("Root 1 =", (-b + math.sqrt(D)) / (2*a))
    print("Root 2 =", (-b - math.sqrt(D)) / (2*a))
elif D == 0:
    print("Two equal real roots")
    print("Root =", -b / (2*a))
else:
    print("Two complex roots")
    print("Root 1 =", complex(-b / (2*a), math.sqrt(-D) / (2*a)))
    print("Root 2 =", complex(-b / (2*a), -math.sqrt(-D) / (2*a)))