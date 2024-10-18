def calculator():

    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    # Введення другого числа
    num2 = float(input("Введіть друге число: "))
    if operation == "+":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Помилка: ділення на 0 неможливе!")
    else:
        print("Помилка: невідома операція!")



calculator()