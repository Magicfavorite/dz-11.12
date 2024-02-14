num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Введите операцию (max, min, avg): ")

if operation == "max":
    result = max(num1, num2, num3)
    print("Максимум из трех чисел:", result)
elif operation == "min":
    result = min(num1, num2, num3)
    print("Минимум из трех чисел:", result)
elif operation == "avg":
    result = (num1 + num2 + num3) / 3
    print("Среднее арифметическое трех чисел:", result)
else:
    print("Некорректная операция!")
