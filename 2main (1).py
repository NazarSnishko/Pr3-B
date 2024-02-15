def power(base, exponent):
    result = 1
    neg_exponent = False
    if exponent < 0:
        neg_exponent = True
        exponent = -exponent
    while exponent:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return 1 / result if neg_exponent else result

# Приклад використання:
base = float(input("Введіть число: "))
exponent = int(input("Введіть степінь: "))
print(f"{base} в степені {exponent} дорівнює {power(base, exponent)}")
