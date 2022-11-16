# Напишите программу которая вводит с клавиатуры номер месяца и день
# и определяет сколько дней осталось до нового года

import datetime
a = int(input())
b = int(input())
final = datetime.date(2022, 12, 31)
user = datetime.date(2022, a, b)
different = final - user
print(f"До нового года осталось {different.days} дней")