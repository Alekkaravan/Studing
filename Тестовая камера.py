number_of_stones1 = int(input())
number_of_stones2 = int(input())

while number_of_stones1 > 0 or number_of_stones2 > 0:
    if number_of_stones1 >= number_of_stones2:
        x1 = number_of_stones1
        x2 = number_of_stones2
        x0 = 1
    else:
        x1 = number_of_stones2
        x2 = number_of_stones1
        x0 = 2
    if x1 == 1:
        AI_bid = 1
        x1 -= AI_bid
    else:
        AI_bid = x1 - 1
        x1 -= AI_bid
    if x0 == 1:
        number_of_stones1, number_of_stones2 = x1, x2
        AI_heap = 1
    else:
        number_of_stones2, number_of_stones1 = x1, x2
        AI_heap = 2
    print(AI_heap, AI_bid, number_of_stones1, number_of_stones2)

    if (number_of_stones1 == 0) and (number_of_stones2 == 0):
        print("ИИ выиграл!")
        break

    players_heap = int(input())
    players_bid = int(input())
    is_bid_ok = False
    while is_bid_ok is False:
        if players_heap == 1 and players_bid <= number_of_stones1 and players_bid > 0:
            is_bid_ok = True
        elif players_heap == 2 and players_bid <= number_of_stones2 and players_bid > 0:
            is_bid_ok = True
        else:
            print("Некорректный ход:", players_heap, players_bid)
            players_heap = int(input())
            players_bid = int(input())
    if players_heap == 1:
        number_of_stones1 -= players_bid
    elif players_heap == 2:
        number_of_stones2 -= players_bid
    print(players_heap, players_bid, number_of_stones1, number_of_stones2)
    if number_of_stones1 == 0 and number_of_stones2 == 0:
        print("Вы выиграли!")
        break

    if number_of_stones1 == 0 and number_of_stones2 == 0:
        print("ИИ выиграли!")
        break

    if number_of_stones1 == 0 and number_of_stones2 == 0:
        print("ИИ выиграли!")
        break
