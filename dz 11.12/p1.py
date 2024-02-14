num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

operation = input("Введите операцию (+ для суммы, * для произведения): ")

if operation == "+":
    result = num1 + num2 + num3
    print("Сумма трех чисел:", result)
elif operation == "*":
    result = num1 * num2 * num3
    print("Произведение трех чисел:", result)
else:
    print("Некорректная операция!")
