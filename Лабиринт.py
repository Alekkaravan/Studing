print("Привет! Добро пожаловать в текстовый квест! Введите что нибудь, что бы начать.")
start = input()
if start == "сладкий рулет":
    print("Вау вы открыли секретную концовку")
    print("Вы попали в Вайтран и стали кузеном стражника. "
          "Пока вы боретесь с драконами ваш кузен охраняет ярла. ")
print("Вы попадаете в закадочное подземелье перед вами 3 двери. "
      "В какую вы пойдёте?(вводите номера дверей, они "
      "номеруются с права на лево)")
Irst = input()
if Irst == "1" or "2" or "3":
    if Irst == "1":
        print("Вы подходите к гномам. ОНи превращают вас в су"
              "щность ввиде гномика")
    elif Irst == "2":
        print("Вас съел троль")
    elif Irst == "3":
        print("Вы попали в комнату с сундуком. "
              "Вы открываете его и забираете два слитка золота"
              "перед вами еще одна развилка с тремя дверьми")
        a = input()
        if a == "1" or "2" or "3":
            if a == "1":
                print("Вас съел морозный паук")
            elif a == "2":
                print("Вы задели нажимную плиту и "
                      "провалились в яму с злокрысам")
                exit()
            elif a == "3":
                print("Вы попали в комнату с гоблинами. "
                      "Они отобрали у вас слиток и пропустили в "
                      "следующую комнату")
                print("Вы опять перед развилка из трёх дверей прев"
                      "ые кажутся очень большими. Похоже за ними зал")
                b = input()
                if b == "1" or "2" or "3":
                    if b == "1":
                        print("Вы вышли к магу."
                              "'Бойся смертный я Мирак, повелитель драконов' "
                              "Он использует "
                              "древний крик и вас вбивает в стену")
                    elif b == "2":
                        print("Вы входите в залу и видите стену с древними "
                              "надписями вы подходите и забирает"
                              "е комплект брони, "
                              "лежащий "
                              "рядом."
                              "Вдруг древняя магия со стены нач"
                              "инает ""переходить к вам. Вы открыли слово силы и нашли"
                              "драконье оружие и броню.")
                        print("Перед Вами появляется отряд при"
                              "зраков. Они обучают Вас словам силы."
                              "с имеющимся вооружением вы унич"
                              "тожаете гоблинов из "
                              "предидущей комнаты. "
                              "Вы поднимаете с их тел "
                              "записку. В ней говорится, что "
                              "вы попали сюда с помощю книги Хермеуса Моры "
                              "- главы этого царства Обливиона."
                              "оказалось, что вы Довакин. Вы вход"
                              "ите в тронный зал Мирака и начинаете бой."
                              "спустя много часов боя и еще б"
                              "ольше зелий лечения"
                              "появляется Хермеус Мора. Он добива"
                              "ет Мирака. Теперь Вы спасли"
                              " Солстхейм - остров с которого"
                              "Вы попали сюда. Хермеус возвращает "
                              "вас домой. Вы - герой")
                    elif b == "3":
                        print("Вы находите древнюю книгу. Она поглащет"
                              " вас. Теперь Вы - раб Мирака")
                else:
                    while b != "1" or "2" or "3":
                        print("К сожалению вы ввели не возможное число. Ва"
                              "м придётся повторить попытку")
                        b = input()
                        if b == "1":
                            print("Вы вышли к магу."
                                  "'Бойся смертный я Мирак, повелитель драконов' "
                                  "Он использует "
                                  "древний крик и вас вбивает в стену")
                            break
                        elif b == "2":
                            print("Вы входите в залу и видите стену с древними "
                                  "надписями вы подходите и забираете комп"
                                  "лект брони, "
                                  "лежащий "
                                  "рядом."
                                  "Вдруг древняя магия со стены начинает "
                                  "переходить к вам. Вы открыли слово силы"
                                  " и нашли"
                                  "драконье оружие и броню.")
                            print("Перед Вами появляется отряд призраков. "
                                  "Они обучают Вас словам силы."
                                  "с имеющимся вооружением вы уничтожаете гоблинов из "
                                  "предидущей комнаты. "
                                  "Вы поднимаете с их тел "
                                  "записку. В ней говорится, что вы попали "
                                  "сюда с помощю книги Хермеуса Моры "
                                  "- главы этого царства Обливион"
                                  "оказалось, что вы Довакин. Вы входите в "
                                  "тронный зал Мирака и начинаете бой."
                                  "спустя много часов боя и еще больше зелий лечения"
                                  "появляется Хермеус Мора. Он "
                                  "добивает Мирака. Теперь Вы спасли"
                                  " Солстхейм - остров с которого"
                                  "Вы попали сюда. Хермеус во"
                                  "звращает вас домой. Вы - герой")
                            break
                        elif b == "3":
                            print("Вы находите древнюю к"
                                  "нигу. Она поглащет вас. Теперь Вы - раб Мирака")
                            break
        while a != "1" or "2" or "3":
            print("К сожалению вы ввели не возможное"
                  " число. Вам придётся повторить попытку")
            a = input()
            if a == "1":
                print("Вас съел морозный паук")
                break
            elif a == "2":
                print("Вы задели нажимную плиту и "
                      "провалились в яму с з"
                      "локрысам")
                break
            elif a == "3":
                print("Вы попали в комнату с гобли"
                      "нами. "
                      "Они отобрали у вас слиток и про"
                      "пустили в "
                      "следующую комнату")
                print("Вы опять перед развилка из трёх двер"
                      "ей превые кажутся очень большими. Похоже за ними зал")
                b = input()
                if b == "1" or "2" or "3":
                    if b == "1":
                        print("Вы вышли к магу."
                              "'Бойся смертный я Мирак, п"
                              "овелитель драконов' "
                              "Он использует "
                              "древний крик и вас вбивает в стену")
                        break
                    elif b == "2":
                        print("Вы входите в залу и видите сте"
                              "ну с древними "
                              "надписями вы подходите и забира"
                              "ете комплект брони, "
                              "лежащий "
                              "рядом."
                              "Вдруг древняя магия со стены на"
                              "чинает ""переходить к вам. Вы отк"
                              "рыли слово силы и нашли"
                              "драконье оружие и броню.")
                        print("Перед Вами появляется отря"
                              "д призраков. Они обучают Вас словам силы."
                              "с имеющимся вооружением вы у"
                              "ничтожаете гоблинов из "
                              "предидущей комнаты. "
                              "Вы поднимаете с их тел "
                              "записку. В ней говорится, что вы"
                              " попали сюда с помощю книги Хермеуса Моры "
                              "- главы этого царства Обливиона."
                              "оказалось, что вы Довакин. Вы входи"
                              "те в тронный зал Мирака и начинаете бой."
                              "спустя много часов боя и еще бол"
                              "ьше зелий лечения"
                              "появляется Хермеус Мора. Он добив"
                              "ает Мирака. Теперь Вы спасли"
                              " Солстхейм - остров с которого"
                              "Вы попали сюда. Хермеус возвращае"
                              "т вас домой. Вы - герой")
                        break
                    elif b == "3":
                        print("Вы находите древнюю книгу. Она погл"
                              "ащет вас. Теперь Вы - раб Мирака")
                        break
                else:
                    while b != "1" or "2" or "3":
                        print("К сожалению вы ввели не возможное "
                              "число. Вам придётся повторить попытку")
                        b = input()
                        if b == "1":
                            print("Вы вышли к магу."
                                  "'Бойся смертный я Мирак, п"
                                  "овелитель драконов' "
                                  "Он использует "
                                  "древний крик и вас вбивает в стену")
                            break
                        elif b == "2":
                            print("Вы входите в залу и видит"
                                  "е стену с древними "
                                  "надписями вы подходите и з"
                                  "абираете комплект брони, "
                                  "лежащий "
                                  "рядом."
                                  "Вдруг древняя магия со стен"
                                  "ы начинает "
                                  "переходить к вам. "
                                  "Вы открыли слово силы и нашли"
                                  "драконье оруж"
                                  "ие и броню.")
                            print(""
                                  "Перед Вами появляется от"
                                  "ряд призраков. Они обучают Вас словам силы."
                                  ""
                                  "с имеющимся вооружен"
                                  "ием вы уничтожаете гоблинов из "
                                  "предидущей комнаты. "
                                  "Вы поднимаете с их тел "
                                  "записку. В ней говорится, что вы"
                                  " попали сюда с помощю книги Хермеуса Моры "
                                  "- главы этого царства Обливиона."
                                  "оказалось, что вы Довакин. Вы "
                                  "входите в тронный зал Мирака и начинаете бой."
                                  "спустя много часов боя"
                                  " и еще больше зелий лечения"
                                  "появляется Хермеус Мора"
                                  ". Он добивает Мирака. Теперь Вы спасли"
                                  " Солстхейм - остров с которого"
                                  "Вы попали сюда. Херме"
                                  "ус возвращает вас домой. Вы - герой")
                            break
                        elif b == "3":
                            print("Вы находите древнюю "
                                  "книгу. Она поглащет вас. Теперь Вы - раб Мирака")
                            break
while Irst != "1" or "2" or "3":
    print("К сожалению вы ввели не возможное чи"
          "сло. Вам придётся повторить попытку")
    Irst = input()
    if Irst == "1":
        print("Вы подходите к гномам. ОНи пре"
              "вращают вас в сущность ввиде гномика")
        break
    elif Irst == "2":
        print("Вас съел троль")
        break
    elif Irst == "3":
        print("Вы попали в комнату с сундуком. "
              "Вы открываете его и забираете два с"
              "литка золота"
              "перед вами еще одна развилка с тремя "
              "дверьми")
        a = input()
        if a == "1" or "2" or "3":
            if a == "1":
                print("Вас съел морозный паук")
                break
            elif a == "2":
                print("Вы задели нажимную плиту и "
                      "провалились в яму с злокрысам")
                break
            elif a == "3":
                print("Вы попали в комнату с гоблинами. "
                      "Они отобрали у вас слиток "
                      "и пропустили в "
                      "следующую комнату")
                print("Вы опять перед развилка из трёх дверей п"
                      "ревые кажутся очень большими. Похоже за ними зал")
                b = input()
                if b == "1" or "2" or "3":
                    if b == "1":
                        print("Вы вышли к магу."
                              "'Бойся смертный я Мирак, повел"
                              "итель драконов' "
                              "Он использует "
                              "древний крик и вас вбивает в стену")
                        break
                    elif b == "2":
                        print("Вы входите в залу и видите стену с древними "
                              "надписями вы подходите и забир"
                              "аете комплект брони, "
                              "лежащий "
                              "рядом."
                              "Вдруг древняя магия со стены начина"
                              "ет ""переходить к вам. Вы открыли слово силы и нашли"
                              "драконье оружие и броню.")
                        print("Перед Вами появляется отряд призрак"
                              "ов. Они обучают Вас словам силы."
                              "с имеющимся вооружением вы уничт"
                              "ожаете гоблинов из "
                              "предидущей комнаты. "
                              "Вы поднимаете с их тел "
                              "записку. В ней говорится, что вы п"
                              "опали сюда с помощю книги Хермеуса Моры "
                              "- главы этого царства Обливиона."
                              "оказалось, что вы Довакин. Вы входите "
                              "в тронный зал Мирака и начинаете бой."
                              "спустя много часов боя и еще больш"
                              "е зелий лечения"
                              "появляется Хермеус Мора. Он добивает Ми"
                              "рака. Теперь Вы спасли"
                              " Солстхейм - остров с которого"
                              "Вы попали сюда. Хермеус возвращает ва"
                              "с домой. Вы - герой")
                        break
                    elif b == "3":
                        print("Вы находите древнюю книгу. Она погл"
                              "ащет вас. Теперь Вы - раб Мирака")
                        break
                else:
                    while b != "1" or "2" or "3":
                        print(" Вам придётся повторить попытку")
                        b = input()
                        if b == "1":
                            print("Вы вышли к магу."
                                  "'Бойся смертный я Мирак, пове"
                                  "литель драконов' "
                                  "Он использует "
                                  "древний крик и вас вбивает в стену")
                            break
                        elif b == "2":
                            print("Вы входите в залу и видите "
                                  "стену с древними "
                                  "надписями вы подходите и з"
                                  "абираете комплект брони, "
                                  "лежащий "
                                  "рядом."
                                  "Вдруг древняя магия со стены начинает "
                                  "переходить к вам. Вы от"
                                  "крыли слово силы и нашли"
                                  "драконье оружие и броню.")
                            print("Перед Вами появляется отряд пр"
                                  "израков. Они обучают Вас словам силы."
                                  "с имеющимся вооружением вы уничтожаете гоблинов из "
                                  "предидущей комнаты. "
                                  "Вы поднимаете с их тел "
                                  "записку. В ней говорится, что вы попа"
                                  "ли сюда с помощю книги Хермеуса Моры "
                                  "- главы этого царства Обливион"
                                  "а."
                                  "оказалось, что вы Довакин."
                                  " Вы входите в тронный зал Мирака и начинаете бой."
                                  "спустя много часов боя и еще больше зелий лечения"
                                  "появляется Хермеус Мора. Он добив"
                                  "ает Мирака. Теперь Вы спасли"
                                  " Солстхейм - остров с которого"
                                  "Вы попали сюда. Хермеус возвращает в"
                                  "ас домой. Вы - герой")
                            break
                        elif b == "3":
                            print("Вы находите древнюю книгу. Она погла"
                                  "щет вас. Теперь Вы - раб Мирака")
                            break
        while a != "1" or "2" or "3":
            print("К сожалению вы ввели не возможное число. Вам придётся пов"
                  "торить попытку")
            a = input()
            if a == "1":
                print("Вас съел морозный паук")
                break
            elif a == "2":
                print("Вы задели нажимную плиту и "
                      "провалились в яму с злокрысам")
                break
            elif a == "3":
                print("Вы попали в комнату с гоблинами. "
                      "Они отобрали у вас слиток и пропустили в "
                      "следующую комнату")
                print("Вы опять перед развилка из трёх дверей превые кажут"
                      "ся очень больши"
                      "ми. Похоже за ними зал")
                b = input()
                if b == "1" or "2" or "3":
                    if b == "1":
                        print("Вы вышли к магу."
                              "'Бойся смертный я Мирак, повелитель драконов' "
                              "Он использует "
                              "древний крик и вас вбивает в стену")
                        break
                    elif b == "2":
                        print("Вы входите в залу и видите стену с древними "
                              "надписями вы подходите и забираете комплект брони, "
                              "лежащий "
                              "рядом."
                              "Вдруг древняя магия со стены начинает "
                              "переходить к вам. Вы открыли слово силы и нашли"
                              "драконье оружие и броню.")
                        print("Перед Вами появляется отряд призраков. Они обучают Вас словам силы."
                              "с имеющимся вооружением вы уничт"
                              "ожаете гоблинов из "
                              "предидущей комнаты. "
                              "Вы поднимаете с их тел "
                              "записку. В ней говорится, что вы попа"
                              "ли сюда с помощю книги Хермеуса Моры "
                              "- главы этого царства Обливиона."
                              "оказалось, что вы Довакин. Вы входите в тронный зал"
                              " Мирака и начинаете бой."
                              "спустя много часов боя и еще больше"
                              " зелий лечения"
                              "появляется Хермеус Мора. Он добивает Мирака. Теперь Вы спасли"
                              " Солстхейм - остров с которого"
                              "Вы попали сюда. Хермеус возвращает вас домой. Вы - герой")
                        break
                    elif b == "3":
                        print("Вы находите древнюю книгу. Она поглащет вас. Теперь Вы - раб"
                              " Мирака")
                        break
                else:
                    while b != "1" or "2" or "3":
                        print("К сожалению вы ввели не возможное числ"
                              "о. Вам придётся повторить попытку")
                        b = input()
                        if b == "1":
                            print("Вы вышли к магу."
                                  "'Бойся смертный я Мирак, повелитель драконов' "
                                  "Он использует "
                                  "древний крик и вас вбивает в стену")
                            break
                        elif b == "2":
                            print("Вы входите в залу и видите стену с древними "
                                  "надписями вы подходите и забираете комплект брони, "
                                  "лежащий "
                                  "рядом."
                                  "Вдруг древняя магия со стены начинает "
                                  "переходить к вам. Вы открыли слово силы и нашли"
                                  "драконье оружие и броню.")
                            print("Перед Вами появляется отряд призраков"
                                  ". Они обучают Вас словам силы."
                                  "с имеющимся вооружением вы уничтожаете гоблинов из "
                                  "предидущей комнаты. "
                                  "Вы поднимаете с их тел "
                                  "записку. В ней говорится, что вы попа"
                                  "ли сюда с помощю книги Хермеуса Моры "
                                  "- главы этого царства Обливиона."
                                  "оказалось, что вы Довакин. Вы вход"
                                  "ите в тронный зал Мирака и начинаете бой."
                                  "спустя много часов боя и еще бол"
                                  "ьше зелий лечения"
                                  "появляется Хермеус Мора. Он добива"
                                  "ет Мирака. Теперь Вы спасли"
                                  " Солстхейм - остров с которого"
                                  "Вы попали сюда. Хермеус возвращает вас домой. Вы - герой")
                            break
                        elif b == "3":
                            print("Вы находите древнюю книгу. Она"
                                  " поглащет вас. Теперь Вы - раб Мирака")
                            break
