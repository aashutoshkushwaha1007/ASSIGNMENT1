num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
    print("Addition:", int(num1) + int(num2))
    print("Substraction:", int(num1) - int(num2))
    print("Multiplication:", int(num1) * int(num2))
    print("Division:", int(num1) / int(num2))
except:
    print("Error: Please enter valid integers.")    