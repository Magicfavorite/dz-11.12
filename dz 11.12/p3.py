meters = float(input("Введите количество метров: "))

unit = input("Введите единицу измерения (mi, in, yd): ")

if unit == "mi":
    result = meters / 1609.34
    print("Мили:", result)
elif unit == "in":
    result = meters * 39.37
    print("Дюймы:", result)
elif unit == "yd":
    result = meters * 1.09361
    print("Ярды:", result)
else:
    print("Некорректная единица измерения!")
