w = int(input("Введите место положение white_figur: "))
b = int(input("Введите место куда нужно пойти: "))
black = int(input("Введи позицию черной фигуры: "))
which_figur = input("фигура: ")
which_figur2 = input("фигура черная: ")
the_board_ = [[11, 21, 31, 41, 51, 61, 71, 81],
              [12, 22, 32, 42, 52, 62, 72, 82],
              [13, 23, 33, 43, 53, 63, 73, 83],
              [14, 24, 34, 44, 54, 64, 74, 84],
              [15, 25, 35, 45, 55, 65, 75, 85],
              [16, 26, 36, 46, 56, 66, 76, 86],
              [17, 27, 37, 47, 57, 67, 77, 87],
              [18, 28, 38, 48, 58, 68, 78, 88]]

if which_figur == "конь":
    list_ = [w + 21, w + 19, w + 12, w + 8, w - 21, w - 19, w - 12, w - 8]
    if b in list_:
        print("Красава")
    else:
        print("Дура")


def diagonals(index_f, index_l):
    diagonal = []
    m = index_f
    for d in the_board_:
        if the_board_.index(d) >= index_l:
            diagonal.append(d[index_f])
            index_f -= 1
            if index_f == -1:
                break
    index_f = m
    for d2 in the_board_:
        if the_board_.index(d2) >= index_l:
            diagonal.append(d2[m])
            m += 1
            if m == 8:
                break

    m = index_f
    for d3 in the_board_[::-1]:
        if the_board_.index(d3) <= index_l:
            diagonal.append(d3[index_f])
            index_f += 1
            if index_f == 8:
                break

    index_f = m
    for d3 in the_board_[::-1]:
        if the_board_.index(d3) <= index_l:
            diagonal.append(d3[index_f])
            index_f -= 1
            if index_f == -1:
                break

    return diagonal


def hod_ver_or_gor(hod):
    index_f = 0
    index_l = 0
    l1 = None
    for i in the_board_:
        for x in i:
            if hod == x:
                l1 = i
                index_l = the_board_.index(i)
                index_f = i.index(hod)
    l = [i[index_f] for i in the_board_]
    l.extend(l1)
    return l, index_f, index_l


if which_figur == "ферьзь":
    a = hod_ver_or_gor(w)
    print(a)
    if b in a[0]:
        print("ты крут чувак")
    d = diagonals(a[1], a[2])
    if b in d:
        print("okay", d)
        if  which_figur2 == "ферьзь":
            bl = hod_ver_or_gor(black)
            bl2 = diagonals(bl[1], bl[2])
            bl2.extend(bl[0])
            if b in bl2:
                print("Чувак тебя схавают")
if which_figur == "пешка":
    # доделать
    for p in the_board_:
        for pp in p:
            if pp == w:
                print(pp, p)
                if b in p:
                    print("good")
if which_figur == "слон":
    for c in the_board_:
        for c_2 in c:
            if w == c_2:
                index_l = the_board_.index(c)
                index_f = c.index(w)
                print(index_l, index_f)
                a = diagonals(index_f, index_l)
                if b in a:
                    print("ход слона")
if which_figur == "ладья":
    hod_ver_or_gor()


def hod_kor():
    hod_korol = []
    for i in the_board_:
        for x in i:
            if x == w:
                index_f = i.index(x)
                if index_f == 0:
                    hod_korol.append(i[index_f + 1])
                elif index_f == 7:
                    hod_korol.append(i[index_f - 1])
                else:
                    hod_korol.append(i[index_f + 1])
                    hod_korol.append(i[index_f - 1])

                index_l = the_board_.index(i)
                for gor in the_board_:
                    if index_l == 0:
                        gor2 = index_l + 1
                        g_ = the_board_[gor2]
                        hod_korol.append(g_[index_f])
                    elif index_l == 7:
                        gor1 = index_l - 1
                        g_ = the_board_[gor1]
                        hod_korol.append(g_[index_f])
                    else:
                        gor1 = index_l - 1
                        gor2 = index_l + 1
                        gr = the_board_[index_l]
                        g_ = gr[index_f]
                        g1 = the_board_[gor1]
                        g2 = the_board_[gor2]
                        hod_korol.append(g1[index_f])
                        hod_korol.append(g2[index_f])
                        hod_korol.append(g_)
                a = diagonals(index_f, index_l)
                try:
                    for j in a:
                        if w == j:
                            index_j = a.index(j)
                            hod_korol.append(a[index_j + 1])
                            a.pop(index_j)
                            a.insert(index_j, 1)
                    hod_korol = set(hod_korol)
                    hod_korol = list(hod_korol)
                    return hod_korol
                except IndexError:
                    hod_korol = set(hod_korol)
                    hod_korol = list(hod_korol)
                    return hod_korol


if which_figur == "король":
    a = hod_kor()
    if b in a:
        print("круто")
    else:
        print("ты Дура")
