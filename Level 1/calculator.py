#Goal: Create a text-based calculator that supports +, -, *, /
#learning outcomes:
# - taking multiple inputs from the user
# - using functions to organize code
# - exception handling (try/except)
# - converting string input to numbers int() float()
# - handling erroes like divisions by zero 

#Challenge: Later, allow multiple operations (2 + 3 * 5)

#try = write a code inside that will cause an error, ex: accepting user input
#except ZeroDivisionError:: division by zero handling
#except ValueError: data type handling
#finally: excute code regradless if there is an exception or not. clean up

def operations():
    cont = "y"
    while cont.lower() == "y":
        operation = input('Enter the operation you want to calculate (+, -, *, /): ')
        if operation not in ["+", "-", "*", "/"]:
            print("Wrong operation. Choose one (+, -, *, /)")
            continue
        try:
            nbr1 = float(input("Enter the first value: "))
            nbr2 = float(input("Enter the second value: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue
        match operation:
            case "+":
                add(nbr1, nbr2)
            case "-":
                subtract(nbr1, nbr2)
            case "*":
                multiply(nbr1, nbr2)
            case "/":
                divide(nbr1, nbr2)
            case _:
                print("Wrong operation. Choose one (+, -, *, /)")
        cont = input("Continue? y/n: ")

def add(nbr1, nbr2):
    result = nbr1 + nbr2
    print(f"{nbr1} + {nbr2} = {result}")

def subtract(nbr1, nbr2):
    result = nbr1 - nbr2
    print(f"{nbr1} - {nbr2} = {result}")

def multiply(nbr1, nbr2):
    result = nbr1 * nbr2
    print(f"{nbr1} * {nbr2} = {result}")

def divide(nbr1, nbr2):
    try:
        result = nbr1 / nbr2 
        print(f"{nbr1} / {nbr2} = {result}")
    except ZeroDivisionError:
        print("Error. you can't divide by zero")
    

operations()