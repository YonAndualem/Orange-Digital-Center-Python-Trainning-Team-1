#Functions
import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def power(x,y):
    return pow(x,y)
def fact(x):
    return (math.factorial (x))
def divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False
def remainder(x,y):
    return (x % y)
def floor_division(x, y):
    return x // y

#UI
print("*** Orange Digital Center Python Trainning***".center(100))
print("********Team 1 - Calculator Project**********".center(100))
print('─' * 100)
print("Welcome to the Calculator, Please select an operation from the list.".center(100))
print("1.Add".center(100))
print("2.Subtract".center(100))
print("3.Multiply".center(100))
print("4.Divide".center(100))
print("5.Power".center(100))
print("6.Factorial".center(100))
print("7.Check Divisiblity".center(100))
print("8. Claculate Remainder".center(100))
print("9. Floor Division".center(100))

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")
#Input
    if choice in ('1', '2', '3', '4','5','7','8','9'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
#IF_Codes
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice=='5':
            print(num1,"^",num2,"=",power(num1,num2))
        elif choice == '7':
            if divisible(num1, num2):
                print("{} is divisible by {}".format(num1, num2))
            else:
                print("{} is not divisible by {}".format(num1, num2))
        elif choice == '8':
            print("The remainder when we divide {} by {} is {}".format(num1, num2, remainder(num1, num2)))
        elif choice == '9':
            print(num1, "//", num2, "=", floor_division(num1, num2))
#Exit_question
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thank you!!!".center(100))
            print('─' * 100)
            break
    elif choice in ('6'):
        num1 = int(input("Enter first number: "))
        print(num1, "!=", fact(num1))

    else:
        print("Invalid Input")
