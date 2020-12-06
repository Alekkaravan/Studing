print("Ваше любимое время года?")
answer1 = input()
answer1 = answer1.lower()
b = 0
if answer1 == "лето":
    b += 1
elif answer1 == "зима":
    b += 2
elif answer1 == "осень":
    b += 3
elif answer1 == "весна":
    b += 0
else:
    print("Вы ввели некорректный вариант")
    exit(0)
print("Ваше любимое животное? (Кот, собака, черепаха)")
answer2 = input()
answer2 = answer2.lower()
if answer2 == "кот":
    b += 1
elif answer2 == "собака":
    b += 0
elif answer2 == "черепаха":
    b += 2
else:
    print("Вы ввели некорректный вариант")
    exit(0)
print("У чего может быть корень")
answer3 = input()
answer3 = answer3.lower()
if answer3 == "дерева":
    b += 1
elif answer3 == "слова":
    b += 0
elif answer3 == "число":
    b += 2
else:
    print("Вы ввели некорректный вариант")
    exit(0)
if b == 0:
    print("Вы обладаете незаурядным умом")
elif b == 1:
    print("Вы умеете вы выбирать друзей")
elif b == 2:
    print("Вы прекрасный оратор")
elif b == 3:
    print("Вы сильная личность")
elif b == 4:
    print("Вы обычный человек")
elif b == 5:
    print("Вы умеете списывать")
elif b == 7:
    print("Ваш IQ 337 вы УМПА-ЛУМПА")
else:
    print("Вы вы вы вы вы вы вы вы вы вы вы вы вы вы вы"
          " вы вы вы вы вы вы вы вы вы сломали систему")
