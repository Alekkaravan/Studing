d = int(input())
a = int(input())
energy = 1
Flag = False
counter = 0
for i in range(a):
    while energy != "КОНЕЦ ЭКСПЕРЕМЕНТА" or energy < 5000:
        energy = input()
        if energy != "КОНЕЦ ЭКСПЕРИМЕНТА":
            energy = int(energy)
        elif energy == "КОНЕЦ ЭКСПЕРИМЕНТА":
            break
        if round(energy / d, 1) - 0.1 == energy // d or round(energy / d, 1) + 0.1 == energy // d:
            counter += 1
            Flag = True
    if Flag:
        print(i + 1, counter)
    counter = 0
    Flag = False
print("Общее количество успешных экспериментов:", a)
