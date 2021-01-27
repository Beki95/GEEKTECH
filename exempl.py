n = int(input("введи 3-x значное число: "))
s = int(input("введи 2-x значное число: "))
print(s+n)

m = """1) ладья и ладья;
2) ладья и  ферзь;
3) ладья и  конь;
4) ладья и  слон;
5) ферзь и  ферзь;
6) ферзь и ладья;
7) ферзь и  конь;
8) ферзь и  слон;
9) конь и  конь;
10) конь и ладья;
11) конь и  ферзь;
12) конь и  слон;
13) слон и  слон;
14) слон и  ферзь;
15) слон и  конь;
16) слон и ладья;
17) король и  слон;
18) король и  ферзь;
19) король и  конь;
20) король и ладья."""
print(m)
while True:
    try:
        n = int(input("Выбери вариант: "))
        if n == 1:
            print("1) ладья и ладья; WIN black")
        elif n == 2:
            print("2) ладья и ферзь; WIN black")
        elif n == 3:
            print("3) ладья и конь; WIN white")
        elif n == 4:
            print("4) ладья и слон; WIN black")
        elif n == 5:
            print("5) ферзь и  ферзь; WIN white")
        elif n == 6:
            print("6) ферзь и ладья; WIN white")
        elif n == 7:
            print("7) ферзь и  конь; Win white")
        elif n == 8:
            print("8) ферзь и  слон; Win white")
        elif n == 9:
            print("9) конь и  конь; Win white")
        elif n == 10:
            print("10) конь и ладья; Win ладья")
        elif n == 11:
            print("11) конь и  ферзь; Win black")
        elif n == 12:
            print("12) конь и  слон; Win black")
        elif n == 13:
            print("13) слон и  слон; Win white")
        elif n == 14:
            print("14) слон и  ферзь; Win white")
        elif n == 15:
            print("15) слон и  конь; Win white")
        elif n == 16:
            print("16) слон и ладья; Win white")
        elif n == 17:
            print("17) король и  слон; Win black")
        elif n == 18:
            print("18) король и  ферзь; Win black")
        elif n == 19:
            print("19) король и  конь; Win white")
        elif n == 20:
            print("20) король и ладья. Win black")
        else:
            print("попробуй еще раз")

    except Exception:
        pass
