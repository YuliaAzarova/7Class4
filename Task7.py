# Программа определяет день недели, соответствующий заданному числу месяца d,
# при условии что в месяце 31 день и первое число понедельник

d = int(input())
nedelya = ["Monday", "Tuesday", "Wensday", "Thusday", "Friday", "Saturday", "Sunday"]
den = d % 7
print(nedelya[den-1])