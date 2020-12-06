a = int(input())
middle = 0
middle_static = 0
for i in range(1, a + 1):
    d = int(input())
    if i == 1 or d == middle_static:
        print("0")
    elif d > middle_static:
        print(">")
    elif d < middle_static:
        print("<")
    middle += d
    middle_static = middle / i
