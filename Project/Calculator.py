a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
operator = input("Enter the Operation: ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
    
elif operator == "*":
    print(a * b)

elif operator == "/":
    print(a / b)
    
else:
    print("Wrong Input")