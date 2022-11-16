n = int(input())
b = str(n)
bnew = list(map(int, b))
proizvedenie = 1
for i in range(len(bnew)):
    proizvedenie *= bnew[i]
print(f"Произведение равно {proizvedenie}, максимальная цифра - {max(bnew)}")