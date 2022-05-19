
def get_napadnuto():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

def ucitaj():
    x = []
    for i in range(8):
        x.append(input())
    return x, get_napadnuto()


def legalan_potez(x, y):
    if x < 0 or y < 0 or x > 7 or y > 7:
        return False
    return True


konj_napad = [
    [-2, -1], [-2, 1], [2, -1], [2, 1],
    [1, 2], [-1, 2], [1, -2], [-1, -2]
]
def konj(napadnuto, i, j):
    for potez in konj_napad:
        if legalan_potez(j + potez[0], i + potez[1]):
            napadnuto[i][j] += 1


def kula(ploca, napadnuto, i, j):
    _i = i
    while _i > 0:
        napadnuto[_i][j] += 1
        if ploca[_i][j] == '#':
            break
        _i -= 1

    _i = i
    while _i < 8:
        napadnuto[_i][j] += 1
        if ploca[_i][j] == '#':
            break
        _i += 1

    _j = j
    while _j > 0:
        napadnuto[i][_j] += 1
        if ploca[i][_j] == '#':
            break
        _j -= 1

    _j = j
    while _j < 8:
        napadnuto[i][_j] += 1
        if ploca[i][_j] == '#':
            break
        _j += 1

def lovac_potez(ploca, napadnuto, i, j, i_ch, j_ch):
    i += i_ch
    j += j_ch
    while legalan_potez(i, j):
        napadnuto[i][j] += 1
        if ploca[i][j] == '#':
            return
        i += i_ch
        j += j_ch
def lovac(ploca, napadnuto, i, j):
    lovac_potez(ploca, napadnuto, i, j, 1, 1)
    lovac_potez(ploca, napadnuto, i, j, -1, 1)
    lovac_potez(ploca, napadnuto, i, j, 1, -1)
    lovac_potez(ploca, napadnuto, i, j, -1, -1)



def kraljica(ploca, napadnuto, i, j):
    kula(ploca, napadnuto, i, j)
    lovac(ploca, napadnuto, i, j)


def ovaj(napadnuto, figurice_poz):
    for i, j in figurice_poz:
        if napadnuto[i][j] == 0:
            return False
    return True

def check_figure(ploca, figurice_poz, i, j):
    napadnuto = get_napadnuto()
    konj(napadnuto, i, j)
    #print(napadnuto)
    if ovaj(napadnuto, figurice_poz):
        return 'knight'

    napadnuto = get_napadnuto()
    lovac(ploca, napadnuto, i, j)
    if ovaj(napadnuto, figurice_poz):
        return 'bishop'

    napadnuto = get_napadnuto()
    kula(ploca, napadnuto, i, j)
    if ovaj(napadnuto, figurice_poz):
        return 'rook'

    napadnuto = get_napadnuto()
    kraljica(ploca, napadnuto, i, j)
    if ovaj(napadnuto, figurice_poz):
        return 'queen'

    return 'impossible'


def napad(ploca, napadnuto):
    figurice = 0
    figurice_poz = []
    for i in range(8):
        for j in range(8):
            if ploca[i][j] == '.':
                continue
            figurice += 1
            konj(napadnuto, i, j)
            kraljica(ploca, napadnuto, i, j)
            figurice_poz.append((i, j))

    for i in range(8):
        for j in range(8):
            if napadnuto[i][j] < figurice:
                continue
            rj = check_figure(ploca, figurice_poz, i, j)
            if rj != 'impossible':
                return rj
    return 'impossible'

def resi():
    ploca, napadnuto = ucitaj()
    print(napad(ploca, napadnuto))

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        resi()
        if i < n - 1:
            input()

