# Программа определяет наименование месяца по его номеру n,
# на выходе строка равная одному из 12 значений

n = int(input())
mesyac = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
print(mesyac[n-1])