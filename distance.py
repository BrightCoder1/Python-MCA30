#Find the distance between two number
import math
a = float(input("Enter the a:"))
b = float(input("Enter the b:"))
c = float(input("Enter the c:"))
d = float(input("Enter the d:"))

distance = math.sqrt((a-b)**2 + (c-d)**2)

print(distance)