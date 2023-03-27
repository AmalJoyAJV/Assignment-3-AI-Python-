# Python project program for simple calculator

# This function adds two numbers
def add(a, j):
    return a + j

# This function subtracts two numbers
def subtract(a, j):
    return a - j

# This function multiplies two numbers
def multiply(a, j):
    return a * j

# This function divides two numbers
def divide(a, j):
    return a / j

# This function ratio two numbers
def ratio(a, j):
    return a ** j


print("Welcome to AJV's calculator, please select the operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Ratio")

while True:
    # take input from the user
    select = input("Select operations from 1/2/3/4/5 : ")

    # check if selected number is one of the five options
    if select in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif select == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif select == '5':
            print(num1, "**", num2, "=", ratio(num1, num2))
        
    # check if user wants another calculation
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "yes":
        input("Press 'Enter' for the next calculation")
    elif next_calculation == "no":
        input("Thank you for using AJV's calculator, Have a nice day!")
        break

    else:
        print("Invalid Input")
        break
