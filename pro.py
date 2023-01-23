
import operator
operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}
def domath(left, operation, right):
    return operations[operation](int(left), int(right))

num1 = input("Enter a number please")
op = input("And operator?")
num2 = input("Lastly put another number in")
print(domath(num1, op, num2)) # The Operation is pro

print("Thanks for using the totally by me calculator!")

reekid = input("please type anything to exit and try again!")