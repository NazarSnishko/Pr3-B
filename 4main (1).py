def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
number = int(input("Введіть число: "))
print(f"Факторіал числа {number} дорівнює {factorial(number)}")
