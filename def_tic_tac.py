import sys

g_d = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
WIN = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
       [1, 4, 7], [2, 5, 8], [3, 6, 9],
       [3, 5, 7], [1, 5, 9]]

x_or_o_2 = ""
game_list = []
game_count = 1


def start():
    global x_or_o, x_or_o_2
    x_or_o_2 = ""
    x_or_o = input("Введи чем хочешь играть: ")
    if x_or_o == "x" or x_or_o == "0":
        if x_or_o == "x":
            x_or_o_2 = "0"
        else:
            x_or_o_2 = "x"
    else:
        start()


def win_game():
    for i, x in zip(WIN, g_d):
        if g_d[i[0]] == g_d[i[1]] == g_d[i[2]] != " ":
            print(f"Выйграл {g_d[i[0]]}")
            sys.exit()
        # elif len(game_list) == 9:
        #     print("ничья")
        #     sys.exit()
    else:
        if len(game_list) == 9:
            print("ничья")
            sys.exit()


def inputs_(game_count):
    start()
    while True:

        game_cart = f"""
                                [ {g_d[1]} | {g_d[2]} | {g_d[3]} ]   
                                [ {g_d[4]} | {g_d[5]} | {g_d[6]} ]   
                                [ {g_d[7]} | {g_d[8]} | {g_d[9]} ] 
                            """
        print(game_cart)
        win_game()
        if game_count == 10:
            break
        if game_count % 2 != 0:
            while True:
                try:
                    user_1 = int(input("enter 1: "))
                    if user_1 in [i for i in range(1, 9 + 1)]:
                        if user_1 not in game_list:
                            game_count += 1
                            game_list.append(user_1)
                            g_d[user_1] = x_or_o
                            break
                        else:
                            print("Это место уже занято")
                    else:
                        print("диапазон чисел от 1 до 9")
                except ValueError:
                    print("Введи число!!!")
        elif game_count % 2 == 0:
            while True:
                try:
                    user_2 = int(input("enter 2: "))
                    if user_2 in [i for i in range(1, 9 + 1)]:
                        if user_2 not in game_list:
                            game_count += 1
                            game_list.append(user_2)
                            g_d[user_2] = x_or_o_2
                            break
                        else:
                            print("Это место уже занято")
                    else:
                        print("диапазон чисел от 1 до 9")
                except ValueError:
                    print("Введи число!!!")

    print(game_count)
    print(game_list)


inputs_(game_count)
