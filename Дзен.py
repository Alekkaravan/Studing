a = input()
b = input()
c = 0
while c != "OK":
    if len(a) < 8:
        print("Короткий!")
    elif "123" in a:
        print("Простой!")
    elif a != b:
        print("Различаются.")
    else:
        c = "OK"
        print(c)
        break
    a = input()
    b = input()
