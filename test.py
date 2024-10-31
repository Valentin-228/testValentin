
try:
    result = input("Введите выражение: ")[:5]
    result.split(sep = None)
    num1 = int(result[0])
    space1 = result[1]
    operator = result[2]
    space2 = result[3]
    num2 = int(result[4])


    if (operator == "+" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 + num2))
    elif (operator == "-" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 - num2))
    elif (operator == "*" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 * num2))
    elif (operator == "/" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 / num2))
    else:
        print("Неверный ввод!")
except IndexError:
    print("Строка не является математической операцией")
except ValueError:
    print("Только целые числа")



