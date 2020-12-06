c = ""
left = 0
right = 1000
while c != "=":
    a = (right + left) // 2
    g = a
    print(a)
    c = input()
    if c == "<":
        right = a
    elif c == ">":
        left = a
