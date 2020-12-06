a = float(input())
b = float(input())
c = input()
d = 0
if c == "+":
    d = a + b
elif c == "-":
    d = a - b
elif c == "/" and b != 0:
    d = a / b
elif c == "*":
    d = a * b
else:
    d = "888888"
print(d)
