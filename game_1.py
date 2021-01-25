# камень, ножницы, бумага игрок против - пк
import random
import sys
import time


class Game:
    game_list = ["ножницы", "камень", "бумага"]
    count_user_game = 0
    count_pk = 0
    count_game = 0

    @staticmethod
    def start():
        print("Привет юзер готов поиграть со мной\nподожди загрузку")
        # for i in range(10):
        #     time.sleep(random.random())
        #     print(".", end="")
        # print()

    @staticmethod
    def again():
        print("Начнем еще раз")
        if Game.count_game == 3:
            Game.count_game = 0
            Game.count_pk = 0
            Game.count_user_game = 0
        Game.games()

    @staticmethod
    def games():
        global user_input
        print("Введи камень, ножницы или бумагу")
        if Game.count_game != 4:
            user_input = input()
        if user_input.isdigit():
            print("ты ввел цифру")
            Game.again()
        else:
            print(f"ок твой ввод {user_input}\n")
            Game.logic()

    @staticmethod
    def stop_game():
        print("Игра окончена")
        Game.result_game()

    @staticmethod
    def logic():
        n = random.choice(Game.game_list)
        Game.count_game += 1
        if Game.count_game != 5:
            if user_input == n:
                print("ничья")
                Game.count_user_game += 0.5
                Game.count_pk += 0.5
                if Game.count_game != 3:
                    Game.again()
                else:
                    Game.stop_game()
            elif user_input == "ножницы":
                if n == "камень":
                    print("Выйграл ПК")
                    Game.count_pk += 1
                else:
                    print("Выйграл User")
                    Game.count_user_game += 1
                if Game.count_game != 3:
                    Game.again()
                else:
                    Game.stop_game()
            elif user_input == "камень":
                if n == "бумага":
                    print("Выйграл ПК")
                    Game.count_pk += 1
                else:
                    print("Выйграл User")
                    Game.count_user_game += 1
                if Game.count_game != 3:
                    Game.again()
                else:
                    Game.stop_game()
            elif user_input == "бумага":
                if n == "ножницы":
                    print("Выйграл ПК")
                    Game.count_pk += 1
                else:
                    print("Выйграл User")
                    Game.count_user_game += 1
                if Game.count_game != 3:
                    Game.again()
                else:
                    Game.stop_game()
        else:
            Game.stop_game()

    @staticmethod
    def result_game():
        if Game.count_user_game > Game.count_pk:
            print("твои очки", Game.count_user_game)
            print(f"очки ПК {Game.count_pk}\nYOU WIN!!!")
        elif Game.count_user_game < Game.count_pk:
            print("твои очки", Game.count_user_game)
            print(f"очки ПК {Game.count_pk}\nYOU LOSE!!!")
        else:
            print("твои очки", Game.count_user_game)
            print(f"очки ПК {Game.count_pk}\nНИЧЬЯ!!!")
        print("Хочешь еще раз сыграть?\nесли да то введи 1\nесли нет то 2")
        m = int(input())
        if m != 1:
            sys.exit()
        else:
            Game.again()


if __name__ == "__main__":
    Game.start()
    Game.games()
