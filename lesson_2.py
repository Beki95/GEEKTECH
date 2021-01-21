a = 100
n = 70
m = a
a = n
n = m
print(a, n)

num1, num2, oper = int(input()), int(input()), input()
result = None
if oper == "+":
    result = lambda num1, num2: num1 + num2
    print(result(num1, num2))
if oper == "-":
    result = lambda num1, num2: num1 - num2
    print(result(num1, num2))
if oper == "*":
    result = lambda num1, num2: num1 * num2
    print(result(num1, num2))
if oper == "/":
    result = lambda num1, num2: num1 / num2
    print(result(num1, num2))



