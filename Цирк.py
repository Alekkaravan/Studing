dictionary = {}
for i in range(int(input())):
    a = input().split()
    b = a[0]
    c = " ".join(a[1:])
    dictionary[b] = c
for i in range(int(input())):
    quiz = input().split()[0]
    a = dictionary.get(quiz)
    if a is None:
        print("Нет в словаре")
    else:
        print(a)
