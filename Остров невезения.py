a = 0
d = "О вкусах не спорят"
print("Как ваше настроение?")
answer = input()
if ("не" in answer) or ("?" in answer):
    print("Простите но я не понял, что вы ввели")
elif ("плох" in answer) or ("грустно" in answer):
    print("Ничего, скоро всё наладится")
elif ("хорош" in answer) or ("прекрасн" in answer):
    print("Отлично, у меня тоже всё хорошо :)")
else:
    print("Простите но я не понял, что вы ввели")
while answer != "До свидания":
    a += 1
    if a == 7:
        a = 1
    if a == 1:
        print("Вы любите кошек? Лично я их обожаю")
        if "не" in answer:
            print(d)
        elif "очень" in answer:
            print("Круто")
        else:
            print("Ясно")
    if a == 2:
        print("А собак?")
        answer = input()
        if "не" in answer:
                print(d)
        elif "очень" in answer:
            print("Интересно")
        else:
            print("Вас понял")
    if a == 3:
        print("Вы играете в компьютерные фильмы")
        answer = input()
        if "да" in answer :
            print("И в какие именно")
            answer = input()
            if 'шут' in answer:
                print("Мне они тоже  нравятся", answer)
            elif 'приключ' in answer:
                print("Мне они тоже  нравятся", answer)
            elif 'гон' in answer:
                print("Мне они тоже  нравятся", answer)
            elif 'аркад' in answer:
                print("Нравится классика? И какой у вас рекорд в динозаврике")
            else:
                print("Не знаю о таком")
