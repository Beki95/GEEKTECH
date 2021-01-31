import sys

cxema = """
    [ 1 | 2 | 3 ]
    [ 4 | 5 | 6 ]
    [ 7 | 8 | 9 ]
     """
print(cxema)
g_d = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
WIN = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
       [1, 4, 7], [2, 5, 8], [3, 6, 9],
       [3, 5, 7], [1, 5, 9]]
user1 = input("Выбери x или o на англ: ")
while True:
    if user1 == "x" or user1 == "o":
        break
    else:
        user1 = input("Выбери x или o на англ: ")
count = 1
input_num1 = None
input_num2 = None
game_list = set()
game_over = 0
while True:
    game_cart = f"""
                [ {g_d[1]} | {g_d[2]} | {g_d[3]} ]   
                [ {g_d[4]} | {g_d[5]} | {g_d[6]} ]   
                [ {g_d[7]} | {g_d[8]} | {g_d[9]} ] 
            """

    for w, x in zip(WIN, g_d):
        try:
            if g_d[w[0]] == g_d[w[1]] == g_d[w[2]] != " ":
                # print(w, x)
                print(f"\n                  ВЫЙГРАЛ: {g_d[w[0]]}")
                print(game_cart)
                game_over += 1
                sys.exit()

        except Exception as ex:
            print(ex)
            pass

    if game_over <= 0 and len(game_list) == 9:
        print("\n                    НИЧЬЯ")
    print(game_cart)
    if count == 10:
        break
        # new_game = input("Если хочешь еще сыграть нажми 1\nесли нет то 2: ")
        # if new_game == str(1):
        #     game_list.clear()
        #     print(game_list)
        #     game_over = 0
        #     count = 1
        #     for d in g_d.items():
        #         g_d[d[0]] = " "
        #     pass
        # else:
        #     break

    user2 = ["x", "o"]
    if user1 == "x":
        user2.remove("x")
    elif user1 == "o":
        user2.remove("o")
    else:
        pass
    # print(user2)

    if count % 2 != 0:
        while True:
            try:
                input_num1 = int(input(f"Введи куда поставить 1={user1}: "))
                if input_num1 not in game_list and 0 < input_num1 <= 9:
                    count += 1
                    break
                elif input_num1 in game_list:
                    print("Это место уже занято")
                    pass
            except ValueError:
                print("Нет такого места попробуй еще раз")
                pass

    elif count % 2 == 0:
        while True:
            try:
                input_num2 = int(input(f"Введи куда поставить 2={user2[0]}: "))
                if input_num2 not in game_list and 0 < input_num1 <= 9:
                    count += 1
                    break
                elif input_num2 in game_list:
                    print("Это место уже занято")
                    pass
            except ValueError:
                print("Нет такого места попробуй еще раз")
                pass

    for i in g_d:
        if input_num1 == i:
            game_list.add(i)
            g_d[i] = user1
        elif input_num2 == i:
            game_list.add(i)
            g_d[i] = user2[0]

    # print(game_list)
    # print(g_d)
    # print(count)
