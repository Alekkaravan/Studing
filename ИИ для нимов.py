a = int(input())
list_word = []
for i in range(a):
    list_word.append(int(input()))
for i in range(a - 1):
    for j in range(a - 1 - i):
        if list_word[j] < list_word[j + 1]:
           list_word[j + 1], list_word[j] = list_word[j], list_word[j + 1]
for i in list_word:
    print(i)
