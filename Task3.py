#Найти сумму цифр 3-х значного числа.

a = int(input())

sotny = a // 100
desaytky = (a - sotny * 100) // 10
edinitsy = a - sotny * 100 - desaytky * 10
print(sotny + desaytky + edinitsy, "- сумма цифр")