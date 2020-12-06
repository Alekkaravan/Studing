"""a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(a) + 2):
    for j in range(len(a) + 2):
        if i == 1 or j == 1 or i == len(a) or j == len(a) + 2:
            print("*", end="")
    print()
"""

a = input().split('?')
b = input()
b[1] = b[1].split("&")
print(b[1])

