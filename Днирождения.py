dictionary = {}
for i in range(int(input())):
    a = input().split()
    b = a[0]
    c = a[2]
    dictionary[c] = b
for i in range(int(input())):
    quiz = input()
    a = dictionary.get(quiz)
    print(a)
