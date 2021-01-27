list_ = [1]
for i in list_:
    num1, num2, oper = int(input("Введи 1 число: ")), int(input("Введи 2 число: ")), input("Введи опер\n"
                                                                         "или же можешь закончить работу\n""Введи что угодно: ")

    if oper == "+":
        result = lambda num1, num2: num1 + num2
    elif oper == "-":
        result = lambda num1, num2: num1 - num2
    elif oper == "*":
        result = lambda num1, num2: num1 * num2
    elif oper == "/":
        result = lambda num1, num2: num1 / num2
    elif oper == "%":
        result = lambda num1, num2: num1 % num2
    elif oper == "**":
        result = lambda num1, num2: num1 ** num2
    else:
        print("Работа закончина!!!")
        break
    list_.append(i)
    print(f"Ваш результат : {result(num1, num2)}")
    print(list_)


