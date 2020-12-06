n = int(input())
x = 1
c = 1
j = 1
while c==n or x<n:
    c = (2*x+j-1)*j/2
    print(x, j, c)
    x+=1
    j+=1

print(j-1)