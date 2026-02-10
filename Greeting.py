firstname=input("Enter your first name:")
lastname=input("Enter your last name:")
try:
    print(f'Hello, {str(firstname)} {str(lastname)}! Welcome to Python programming.')
except:
    print("Error: Please enter valid names.")