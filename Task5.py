# Идёт k-я секунда суток. Определить,
# сколько целых часов h и целых минут m прошло с начала суток

k = int(input())
h = k // 3600
m = (k - h * 3600) // 60
print(f"It's {h} hours, {m} minutes")