# Вводятся 2 числа. Если оба четные , на экран выдается 2,
# если оба нечетные , то выведите 1,
# Если различные , выведите 0.

a = int(input())
b = int(input())
if a % 2 == 0 and b % 2 == 0:
    print("2")
elif a % 2 == 1 and b % 2 == 1:
    print("1")
else:
    print("0")