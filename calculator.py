#hello this is a program which is simple condition based calculation
#Thank You!


print("Use * for multiplication  + for additon \n - for subtraction  / for division ** for exponention")

selection = input("Enter your selection:")

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

if selection == '*':
    print("Result:", a*b)

elif selection == '/':
    print("Result",a/b)

elif selection == '-':
    print("Result",a-b)

elif selection == '+':
    print("Result",a+b)

elif selection == '**':
    c = float(input("Enter the number:"))
    print("Result",c*c)

else:
    print("Please enter the valid value!")
