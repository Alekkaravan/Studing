a = int(input())
n = ""
d = 0
for i in range(1, a + 1):
    if a % i == 0:
        n += str(i)
        if i != a:
            n += " "
        d += 1
print(n)
if d != 2:
    print("НЕТ")
else:
    print("ПРОСТОЕ")
