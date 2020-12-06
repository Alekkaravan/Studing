print("Вы находитесь в комнате перед вами три двери, в какую пойдёте?")
print("(Вводите цифры, либо напишите 0, что бы вернуться к предидущей развилке)")
a = int(input())
inventory = 0
counter_of_guests1 = 0
error = "к сожалению вы выбрали не тот ответ, повторите снова"
Dead = "Вы упали в яму со змеями"
number_of_fork = 0
while number_of_fork >= 0:
    if number_of_fork == 0 and a == 1 and counter_of_guests1 == 0:
        print("Вы вошли в комнату со столом. Вы осматриваете стол и находите в нём отмычку и нож")
        print("Теперь они ваши. Перед вами три двери, в какую пойдёте?")
        inventory += 1
        number_of_fork += 1
        counter_of_guests1 += 1
    elif number_of_fork == 0 and a == 1 and counter_of_guests1 != 0:
        print("Вы вошли в комнату со столом.")
        print("Перед вами три двери, в какую пойдёте?")
        number_of_fork += 1
    elif number_of_fork == 0 and a == 2 and inventory == 1:
        print("Вы пытаетесь взломать дверь из которой веет воздухом, но отмычка ломается")
        print("Найди справочник")
        print("Перед вами три двери, в какую пойдёте?")
        inventory -= 0.5
    elif number_of_fork == 0 and a == 2 and inventory >= 2:
        print("Вы смогли вскрыть дверь")
        print("Вы выбрались из лабиринта")
        print("ПОБЕДА!")
        break
    elif number_of_fork == 0 and a == 2 and inventory < 1:
        print('Вы не можете пройти дальше, но от туда дует ветер, там выход.')
        print('"Вам нужно взломать замок", - гласит надпись на двери')
        print("Вы всё в той же комнате перед вами всё ещё три двери")
    elif number_of_fork == 0 and a == 3:
        print(Dead)
        break
    elif number_of_fork == 1 and a == 2:
        print("Вы дошли до библиотеки. С помощью реестра книг вы наши справочник по взлому замков")
        print("В библиотеке нет дверей, но можно вернуться назад")
        number_of_fork += 1
        inventory += 1
    elif number_of_fork == 1 and a == 3:
        print("Вы нашли золотохранилище и забираете всё что можете унести и отмычки")
        print("Из золотохранилища ведёт три двери не считая той из которой вы пришли")
        number_of_fork += 1
        inventory += 1
    elif number_of_fork == 1 and a == 1:
        print(Dead)
        break
    elif number_of_fork == 2 and a != 0:
        print("На вас напали пиглины и убили вас")
        break
    elif a == 0:
        print("Вы вернулись к предидущей развилке")
        print("Вы находитесь в комнате перед вами три двери, в какую пойдёте?")
        number_of_fork -= 1
    else:
        print(error)
    a = int(input())
