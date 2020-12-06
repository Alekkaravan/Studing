line = input().split(" ")
stack = []
for char in line:
    if char in ["+", "-", "*"]:
        if char == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif char == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif char == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
    else:
        stack.append(int(char))
print(stack.pop())
