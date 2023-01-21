num1 = float(input("Hello there! Im the improved calculator! Please enter your number>>>:"))
op = input("Enter the operator!>>>:")
num2 = float(input("Then Finally! Please enter your number>>>:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Sorry that is not one of the 4 main operators! Please choose addition which is +, subtract is -,multiply is *, and finally divide is /!")


reekid = input("please type anything to exit and try again!")