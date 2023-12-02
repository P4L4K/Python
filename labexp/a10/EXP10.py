#Write a program to create a Simple Calculator using a switch case and function for every operation. 

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero!"
while True:
    print("""MENU:
    1: Add
    2: Subtract
    3: Multiply
    4: Divide
    5: Exit""")
    choice = input("Enter choice (1-5): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")


