from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
number = int(input("Введіть число: "))
print(f"Факторіал числа {number} дорівнює {factorial(number)}")
