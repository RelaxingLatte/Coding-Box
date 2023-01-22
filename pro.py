
import operator
operations = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}
def domath(left, operation, right):
    return operations[operation](int(left), int(right))

num1 = input()
op = input()
num2 = input()
print(domath(num1, op, num2)) #prints 150



reekid = input("please type anything to exit and try again!")