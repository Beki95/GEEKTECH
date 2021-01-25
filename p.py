import random
import sys


class Test():

    random_num = random.randint(1000, 9999)
    n = int(input("Введи 4 числа: "))

    def game(self):
        if Test.n == Test.random_num:
            print("Ты угадал")
            sys.exit()
        else:
            print("Ты не угодал")
            print(Test.random_num)
            Test.n = int(input("введи 4 числа: "))
            self.game()


a = Test()
a.game()
