import random


class Game:
    dict_ = {
        "d1": 1, "d2": 2, "d3": 3,
        "d4": 4, "d5": 5, "d6": 6,
        "d7": 7, "d8": 8, "d9": 9,
    }
    list_num = [1, 2, 3, 4, 6, 5, 7, 8, 9]

    @staticmethod
    def user_input_f():
        global user_input
        user_input = int(input("Введи куда поставить: "))

    @staticmethod
    def check():
        global x_or_o
        x_or_o = input("Введи только x или o: ")
        if x_or_o == "x" or x_or_o == "o":
            Game.user_input_f()
        else:
            Game.check()

    @staticmethod
    def komp():
        list_choice = ["x", "o"]
        if x_or_o == "x":
            list_choice.remove("x")
        elif x_or_o == "o":
            list_choice.remove("o")
        print(list_choice[0])
        if len(Game.list_num) == 0:
            print("ВСЕ")
        else:
            n = random.choice(Game.list_num)
            print(n)

    @staticmethod
    def game():
        if str(
                user_input) in f'{Game.dict_["d1"]}{Game.dict_["d2"]}{Game.dict_["d3"]}' \
                               f'{Game.dict_["d4"]}{Game.dict_["d5"]}{Game.dict_["d6"]}' \
                               f'{Game.dict_["d7"]}{Game.dict_["d8"]}{Game.dict_["d9"]}':
            if user_input == Game.dict_["d1"]:
                Game.dict_.update(d1=f"{x_or_o}")
                Game.list_num.remove(1)
            elif user_input == Game.dict_["d2"]:
                Game.dict_.update(d2=f"{x_or_o}")
                Game.list_num.remove(2)
            elif user_input == Game.dict_["d3"]:
                Game.dict_.update(d3=f"{x_or_o}")
                Game.list_num.remove(3)
            elif user_input == Game.dict_["d4"]:
                Game.dict_.update(d4=f"{x_or_o}")
                Game.list_num.remove(4)
            elif user_input == Game.dict_["d5"]:
                Game.dict_.update(d5=f"{x_or_o}")
                Game.list_num.remove(5)
            elif user_input == Game.dict_["d6"]:
                Game.dict_.update(d6=f"{x_or_o}")
                Game.list_num.remove(6)
            elif user_input == Game.dict_["d7"]:
                Game.dict_.update(d7=f"{x_or_o}")
                Game.list_num.remove(7)
            elif user_input == Game.dict_["d8"]:
                Game.dict_.update(d8=f"{x_or_o}")
                Game.list_num.remove(8)
            else:
                Game.dict_.update(d9=f"{x_or_o}")
                Game.list_num.remove(9)

        m = f"""
        {Game.dict_["d1"]} | {Game.dict_["d2"]} | {Game.dict_["d3"]}
        {Game.dict_["d4"]} | {Game.dict_["d5"]} | {Game.dict_["d6"]}
        {Game.dict_["d7"]} | {Game.dict_["d8"]} | {Game.dict_["d9"]}
    """
        print(m)
        print(Game.list_num)
        Game.komp()
        Game.user_input_f()
        Game.game()


if __name__ == '__main__':
    g = Game
    g.check()
    g.game()
