a = int(input())
a = list(str(a))
b = []
for i in a:
    b.append(int(i))
c = b[0] + b[1]
d = b[1] + b[2]
if c > d:
    r = int(str(c) + str(d))
else:
    r = int(str(d) + str(c))
print(r)
