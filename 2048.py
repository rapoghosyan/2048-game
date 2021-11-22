import random


def prn():
    global res, a
    for f in range(28):
        for g in range(68):
            res[f][g] = ' '
    for f in range(4):
        for g in range(4):
            app(f, g, a[f][g])
    print('╔', end='')
    for _ in range(3):
        for q in range(17):
            print('=', end='')
        print('╦', end='')
    for q in range(17):
        print('=', end='')
    print('╗')
    for t in range(3):
        for x in range(t * 7, (t + 1) * 7):
            print('║', end='')
            for q in range(3):
                for y in range(q * 17, (q + 1) * 17):
                    print(res[x][y], end='')
                print('│', end='')
            for y in range(51, 68):
                print(res[x][y], end='')
            print('║', end='')
            print()
        print('╠', end='')
        for _ in range(3):
            for q in range(17):
                print('-', end='')
            print('┼', end='')
        for q in range(17):
            print('-', end='')
        print('╣')
    for x in range(21, 28):
        print('║', end='')
        for q in range(3):
            for y in range(q * 17, (q + 1) * 17):
                print(res[x][y], end='')
            print('│', end='')
        for y in range(51, 68):
            print(res[x][y], end='')
        print('║', end='')
        print()
    print('╚', end='')
    for _ in range(3):
        for q in range(17):
            print('=', end='')
        print('╩', end='')
    for q in range(17):
        print('=', end='')
    print('╝')


def app(x, y, z):
    global res
    temp = []
    for q in range(7):
        temp.append([])
        for w in range(17):
            temp[q].append(' ')
    if z != 0:
        if z == 2:
            temp[0][5] = '*'
            temp[0][6] = '*'
            temp[0][7] = '*'
            temp[0][8] = '*'
            temp[0][9] = '*'
            temp[0][10] = '*'
            temp[0][11] = '*'
            temp[1][11] = '*'
            temp[2][11] = '*'
            temp[3][6] = '*'
            temp[3][7] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[4][5] = '*'
            temp[5][5] = '*'
            temp[6][5] = '*'
            temp[6][6] = '*'
            temp[6][7] = '*'
            temp[6][8] = '*'
            temp[6][9] = '*'
            temp[6][10] = '*'
            temp[6][11] = '*'
        elif z == 4:
            temp[0][5] = '*'
            temp[0][11] = '*'
            temp[1][5] = '*'
            temp[1][11] = '*'
            temp[2][5] = '*'
            temp[2][11] = '*'
            temp[3][5] = '*'
            temp[3][6] = '*'
            temp[3][7] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][11] = '*'
            temp[5][11] = '*'
            temp[6][11] = '*'
        elif z == 8:
            temp[0][5] = '*'
            temp[0][6] = '*'
            temp[0][7] = '*'
            temp[0][8] = '*'
            temp[0][9] = '*'
            temp[0][10] = '*'
            temp[0][11] = '*'
            temp[1][5] = '*'
            temp[1][11] = '*'
            temp[2][5] = '*'
            temp[2][11] = '*'
            temp[3][5] = '*'
            temp[3][6] = '*'
            temp[3][7] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][5] = '*'
            temp[4][11] = '*'
            temp[5][5] = '*'
            temp[5][11] = '*'
            temp[6][5] = '*'
            temp[6][6] = '*'
            temp[6][7] = '*'
            temp[6][8] = '*'
            temp[6][9] = '*'
            temp[6][10] = '*'
            temp[6][11] = '*'
        elif z == 16:
            temp[0][5] = '*'
            temp[1][5] = '*'
            temp[2][5] = '*'
            temp[3][5] = '*'
            temp[4][5] = '*'
            temp[5][5] = '*'
            temp[6][5] = '*'
            temp[1][4] = '*'
            temp[2][3] = '*'
            temp[3][2] = '*'
            temp[0][8] = '*'
            temp[0][9] = '*'
            temp[0][10] = '*'
            temp[0][11] = '*'
            temp[0][12] = '*'
            temp[0][13] = '*'
            temp[0][14] = '*'
            temp[1][8] = '*'
            temp[2][8] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[4][8] = '*'
            temp[4][14] = '*'
            temp[5][8] = '*'
            temp[5][14] = '*'
            temp[6][8] = '*'
            temp[6][9] = '*'
            temp[6][10] = '*'
            temp[6][11] = '*'
            temp[6][12] = '*'
            temp[6][13] = '*'
            temp[6][14] = '*'
        elif z == 32:
            temp[0][1] = '*'
            temp[0][2] = '*'
            temp[0][3] = '*'
            temp[0][4] = '*'
            temp[0][5] = '*'
            temp[0][6] = '*'
            temp[0][7] = '*'
            temp[1][7] = '*'
            temp[2][7] = '*'
            temp[3][1] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[3][4] = '*'
            temp[3][5] = '*'
            temp[3][6] = '*'
            temp[3][7] = '*'
            temp[4][7] = '*'
            temp[5][7] = '*'
            temp[6][1] = '*'
            temp[6][2] = '*'
            temp[6][3] = '*'
            temp[6][4] = '*'
            temp[6][5] = '*'
            temp[6][6] = '*'
            temp[6][7] = '*'
            temp[0][9] = '*'
            temp[0][10] = '*'
            temp[0][11] = '*'
            temp[0][12] = '*'
            temp[0][13] = '*'
            temp[0][14] = '*'
            temp[0][15] = '*'
            temp[1][15] = '*'
            temp[2][15] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[4][9] = '*'
            temp[5][9] = '*'
            temp[6][9] = '*'
            temp[6][10] = '*'
            temp[6][11] = '*'
            temp[6][12] = '*'
            temp[6][13] = '*'
            temp[6][14] = '*'
            temp[6][15] = '*'
        elif z == 64:
            temp[0][1] = '*'
            temp[0][2] = '*'
            temp[0][3] = '*'
            temp[0][4] = '*'
            temp[0][5] = '*'
            temp[0][6] = '*'
            temp[0][7] = '*'
            temp[1][1] = '*'
            temp[2][1] = '*'
            temp[3][1] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[3][4] = '*'
            temp[3][5] = '*'
            temp[3][6] = '*'
            temp[3][7] = '*'
            temp[4][1] = '*'
            temp[4][7] = '*'
            temp[5][1] = '*'
            temp[5][7] = '*'
            temp[6][1] = '*'
            temp[6][2] = '*'
            temp[6][3] = '*'
            temp[6][4] = '*'
            temp[6][5] = '*'
            temp[6][6] = '*'
            temp[6][7] = '*'
            temp[0][9] = '*'
            temp[0][15] = '*'
            temp[1][9] = '*'
            temp[1][15] = '*'
            temp[2][9] = '*'
            temp[2][15] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[3][15] = '*'
            temp[4][15] = '*'
            temp[5][15] = '*'
            temp[6][15] = '*'
        elif z == 128:
            temp[1][4] = '*'
            temp[2][4] = '*'
            temp[3][4] = '*'
            temp[4][4] = '*'
            temp[5][4] = '*'
            temp[2][3] = '*'
            temp[3][2] = '*'
            temp[1][7] = '*'
            temp[1][8] = '*'
            temp[1][9] = '*'
            temp[2][9] = '*'
            temp[3][7] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[4][7] = '*'
            temp[5][7] = '*'
            temp[5][8] = '*'
            temp[5][9] = '*'
            temp[1][12] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[2][12] = '*'
            temp[2][14] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[4][12] = '*'
            temp[4][14] = '*'
            temp[5][12] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
        elif z == 256:
            temp[1][2] = '*'
            temp[1][3] = '*'
            temp[1][4] = '*'
            temp[2][4] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[3][4] = '*'
            temp[4][2] = '*'
            temp[5][2] = '*'
            temp[5][3] = '*'
            temp[5][4] = '*'
            temp[1][7] = '*'
            temp[1][8] = '*'
            temp[1][9] = '*'
            temp[2][7] = '*'
            temp[3][7] = '*'
            temp[3][8] = '*'
            temp[3][9] = '*'
            temp[4][9] = '*'
            temp[5][7] = '*'
            temp[5][8] = '*'
            temp[5][9] = '*'
            temp[1][12] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[2][12] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[4][12] = '*'
            temp[4][14] = '*'
            temp[5][12] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
        elif z == 512:
            temp[1][2] = '*'
            temp[1][3] = '*'
            temp[1][4] = '*'
            temp[2][2] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[3][4] = '*'
            temp[4][4] = '*'
            temp[5][2] = '*'
            temp[5][3] = '*'
            temp[5][4] = '*'
            temp[1][9] = '*'
            temp[2][9] = '*'
            temp[3][9] = '*'
            temp[4][9] = '*'
            temp[5][9] = '*'
            temp[2][8] = '*'
            temp[3][7] = '*'
            temp[1][12] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[2][14] = '*'
            temp[3][12] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[4][12] = '*'
            temp[5][12] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
        elif z == 1024:
            temp[1][3] = '*'
            temp[2][3] = '*'
            temp[3][3] = '*'
            temp[4][3] = '*'
            temp[5][3] = '*'
            temp[2][2] = '*'
            temp[3][1] = '*'
            temp[1][5] = '*'
            temp[1][6] = '*'
            temp[1][7] = '*'
            temp[2][5] = '*'
            temp[2][7] = '*'
            temp[3][5] = '*'
            temp[3][7] = '*'
            temp[4][5] = '*'
            temp[4][7] = '*'
            temp[5][5] = '*'
            temp[5][6] = '*'
            temp[5][7] = '*'
            temp[1][9] = '*'
            temp[1][10] = '*'
            temp[1][11] = '*'
            temp[2][11] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][9] = '*'
            temp[5][9] = '*'
            temp[5][10] = '*'
            temp[5][11] = '*'
            temp[1][13] = '*'
            temp[1][15] = '*'
            temp[2][13] = '*'
            temp[2][15] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[3][15] = '*'
            temp[4][15] = '*'
            temp[5][15] = '*'
        elif z == 2048:
            temp[1][1] = '*'
            temp[1][2] = '*'
            temp[1][3] = '*'
            temp[2][3] = '*'
            temp[3][1] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[4][1] = '*'
            temp[5][1] = '*'
            temp[5][2] = '*'
            temp[5][3] = '*'
            temp[1][5] = '*'
            temp[1][6] = '*'
            temp[1][7] = '*'
            temp[2][5] = '*'
            temp[2][7] = '*'
            temp[3][5] = '*'
            temp[3][7] = '*'
            temp[4][5] = '*'
            temp[4][7] = '*'
            temp[5][5] = '*'
            temp[5][6] = '*'
            temp[5][7] = '*'
            temp[1][9] = '*'
            temp[1][11] = '*'
            temp[2][9] = '*'
            temp[2][11] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][11] = '*'
            temp[5][11] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[1][15] = '*'
            temp[2][13] = '*'
            temp[2][15] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[3][15] = '*'
            temp[4][13] = '*'
            temp[4][15] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
            temp[5][15] = '*'
            for q in [0, 6]:
                for w in [0, 8, 16]:
                    temp[q][w] = '®'
        elif z == 4096:
            temp[1][1] = '*'
            temp[1][3] = '*'
            temp[2][1] = '*'
            temp[2][3] = '*'
            temp[3][1] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[4][3] = '*'
            temp[5][3] = '*'
            temp[1][5] = '*'
            temp[1][6] = '*'
            temp[1][7] = '*'
            temp[2][5] = '*'
            temp[2][7] = '*'
            temp[3][5] = '*'
            temp[3][7] = '*'
            temp[4][5] = '*'
            temp[4][7] = '*'
            temp[5][5] = '*'
            temp[5][6] = '*'
            temp[5][7] = '*'
            temp[1][9] = '*'
            temp[1][10] = '*'
            temp[1][11] = '*'
            temp[2][9] = '*'
            temp[2][11] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][11] = '*'
            temp[5][9] = '*'
            temp[5][10] = '*'
            temp[5][11] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[1][15] = '*'
            temp[2][13] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[3][15] = '*'
            temp[4][13] = '*'
            temp[4][15] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
            temp[5][15] = '*'
        elif z == 8192:
            temp[1][1] = '*'
            temp[1][2] = '*'
            temp[1][3] = '*'
            temp[2][1] = '*'
            temp[2][3] = '*'
            temp[3][1] = '*'
            temp[3][2] = '*'
            temp[3][3] = '*'
            temp[4][1] = '*'
            temp[4][3] = '*'
            temp[5][1] = '*'
            temp[5][2] = '*'
            temp[5][3] = '*'
            temp[1][7] = '*'
            temp[2][7] = '*'
            temp[3][7] = '*'
            temp[4][7] = '*'
            temp[5][7] = '*'
            temp[2][6] = '*'
            temp[3][5] = '*'
            temp[1][9] = '*'
            temp[1][10] = '*'
            temp[1][11] = '*'
            temp[2][9] = '*'
            temp[2][11] = '*'
            temp[3][9] = '*'
            temp[3][10] = '*'
            temp[3][11] = '*'
            temp[4][11] = '*'
            temp[5][9] = '*'
            temp[5][10] = '*'
            temp[5][11] = '*'
            temp[1][13] = '*'
            temp[1][14] = '*'
            temp[1][15] = '*'
            temp[2][15] = '*'
            temp[3][13] = '*'
            temp[3][14] = '*'
            temp[3][15] = '*'
            temp[4][13] = '*'
            temp[5][13] = '*'
            temp[5][14] = '*'
            temp[5][15] = '*'
        for q in range(7):
            for w in range(17):
                res[7 * x + q][17 * y + w] = temp[q][w]


def step():
    global gor
    x = gor[0]
    y = gor[1]
    z = gor[2]
    q = gor[3]
    e = gor[4]
    if q == 0:
        if z == 0:
            if y == 0:
                q = x
                x = 0
                if q != 0:
                    e = 1
            elif y == x:
                q = 2 * x
                x = 0
                y = 0
                e = 1
            else:
                q = y
                z = x
                x = 0
                y = 0
                e = 1
        elif y == 0:
            if x == z:
                q = 2 * x
                x = 0
                z = 0
                e = 1
            else:
                q = z
                z = x
                x = 0
                e = 1
        elif y == z:
            q = 2 * y
            z = x
            x = 0
            e = 1
        elif x == y:
            q = z
            z = 2 * x
            y = 0
            x = 0
            e = 1
        else:
            q = z
            z = y
            y = x
            x = 0
            e = 1
    elif z == 0:
        if y == 0:
            if x == q:
                q = 2 * x
                x = 0
                e = 1
            elif x != 0:
                z = x
                x = 0
                e = 1
        elif q == y:
            q = 2 * y
            z = x
            y = 0
            x = 0
            e = 1
        elif y == x:
            z = 2 * y
            y = 0
            x = 0
            e = 1
        else:
            z = y
            y = x
            x = 0
            e = 1
    elif y == 0:
        if q == z:
            q = 2 * z
            z = x
            x = 0
            e = 1
        elif z == x:
            z = 2 * x
            x = 0
            e = 1
        elif x != 0:
            y = x
            x = 0
            e = 1
    elif q == z:
        if y == x:
            q = 2 * z
            z = 2 * x
            y = 0
            x = 0
            e = 1
        else:
            q = 2 * z
            z = y
            y = x
            x = 0
            e = 1
    elif z == y:
        z = 2 * y
        y = x
        x = 0
        e = 1
    elif y == x:
        y = 2 * x
        x = 0
        e = 1
    if e == 1:
        gor[0] = x
        gor[1] = y
        gor[2] = z
        gor[3] = q
        gor[4] = e


a = []
b = []
for i in range(4):
    a.append([])
    b.append([])
    for j in range(4):
        a[i].append(0)
        b[i].append(0)
c = []
for i in range(16):
    c.append([0])
res = []
for i in range(28):
    res.append([])
    for j in range(68):
        res[i].append(' ')
last = []
for i in range(5):
    last.append('')

print('Hello!')
print('This is game 2048')
game = 1
while game == 1:
    h = random.randint(1, 6)
    for i in range(4):
        for j in range(4):
            a[i][j] = 0
    for k in range(16):
        c[k] = 0
    k = 1
    for i in range(4):
        for j in range(4):
            if a[i][j] == 0:
                c[k - 1] = 10 * i + j
                k += 1
    if k != 1:
        k -= 1
        k = random.randint(0, k - 1)
        if h == 6:
            h = 4
        else:
            h = 2
        i = c[k] // 10
        j = c[k] % 10
        a[i][j] = h
    prn()
    for i in range(4):
        for j in range(4):
            b[i][j] = a[i][j]
    print('Please press')
    print(' w - for up')
    print(' s - for down')
    print(' a - for left')
    print(' d - for right')
    print('  u - for going back 1 step')
    print()
    print(' r - for restart')
    print('And f - for finish game')
    print()
    possibility = 1
    st = 1
    last[1] = 'l'
    last[2] = 'l'
    last[3] = 'l'
    last[4] = 'l'
    while possibility == 1 and game == 1:
        st = 0
        if last[4] == 'u':
            s = 'u'
        else:
            s = input()
            p = 1
            if last[3] == 'w':
                if s == 'w' or s == 's':
                    p = 0
            if last[2] == 'a':
                if s == 'a' or s == 'd':
                    p = 0
            if p == 1:
                if s == 'w' or s == 's' or s == 'a' or s == 'd':
                    for i in range(4):
                        for j in range(4):
                            b[i][j] = a[i][j]
            if p == 1:
                if s == 'w':
                    for i in range(4):
                        gor = [a[3][i], a[2][i], a[1][i], a[0][i], st]
                        step()
                        a[3][i] = gor[0]
                        a[2][i] = gor[1]
                        a[1][i] = gor[2]
                        a[0][i] = gor[3]
                        st = gor[4]
                elif s == 's':
                    for i in range(4):
                        gor = [a[0][i], a[1][i], a[2][i], a[3][i], st]
                        step()
                        a[0][i] = gor[0]
                        a[1][i] = gor[1]
                        a[2][i] = gor[2]
                        a[3][i] = gor[3]
                        st = gor[4]
                elif s == 'a':
                    for i in range(4):
                        gor = [a[i][3], a[i][2], a[i][1], a[i][0], st]
                        step()
                        a[i][3] = gor[0]
                        a[i][2] = gor[1]
                        a[i][1] = gor[2]
                        a[i][0] = gor[3]
                        st = gor[4]
                elif s == 'd':
                    for i in range(4):
                        gor = [a[i][0], a[i][1], a[i][2], a[i][3], st]
                        step()
                        a[i][0] = gor[0]
                        a[i][1] = gor[1]
                        a[i][2] = gor[2]
                        a[i][3] = gor[3]
                        st = gor[4]
                elif s == 'f':
                    game = 0
                elif s == 'r':
                    possibility = 0
                elif s == 'u':
                    if last[1] == 'u':
                        for i in range(4):
                            for j in range(4):
                                a[i][j] = b[i][j]
                        prn()
                    else:
                        print('Sorry, you can not do undo')
                        print('Please, select another step')
                if st == 1:
                    last[1] = 'u'
                    for k in range(16):
                        c[k] = 0
                    k = 1
                    for i in range(4):
                        for j in range(4):
                            if a[i][j] == 0:
                                c[k - 1] = 10 * i + j
                                k += 1
                    if k != 1:
                        k -= 1
                        k = random.randint(0, k - 1)
                        h = random.randint(1, 6)
                        if h == 6:
                            h = 4
                        else:
                            h = 2
                        i = c[k] // 10
                        j = c[k] % 10
                        a[i][j] = h
                    prn()
                    possibility = 2
                    for i in range(4):
                        for j in range(3):
                            if a[i][j] == 0 or a[i][j + 1] == 0 or a[i][j] == a[i][j + 1]:
                                possibility = 1
                    if possibility == 2:
                        last[2] = 'a'
                    possibility = 2
                    for i in range(4):
                        for j in range(3):
                            if a[j][i] == 0 or a[j + 1][i] == 0 or a[j][i] == a[j + 1][i]:
                                possibility = 1
                    if possibility == 2:
                        last[3] = 'w'
                    possibility = 1
                    if last[2] == 'a' and last[3] == 'w':
                        print('Please press')
                        print(' u - for undo')
                        print(' f - for finish')
                        print(' or any other key - for restart')
                        s = input()
                if st == 1:
                    if last[2] == 'a' and last[3] == 'w':
                        if s == 'f':
                            game = 0
                        elif s == 'u':
                            last[4] = 'u'
                            last[2] = 'l'
                            last[3] = 'l'
                        else:
                            possibility = 0
                    else:
                        last[1] = 'u'
                elif s == 'w' or s == 's' or s == 'a' or s == 'd':
                    print('Your step is invalid')
                    print('Please, select another step')
                elif s != 'r' and s != 'f' and s != 'u':
                    print('Your step does not exist')
                    print('Please, select a right step')
