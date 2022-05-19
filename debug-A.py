from math import floor

def compare(a):
    return a[1]

def izracunaj_vrijeme(zadatak, patkica):
    return floor(zadatak[0][1] / (zadatak[0][0] + patkica[0]))


def brute_force(zadatak, patkica):
    if len(patkica) == 1 or len(zadatak) == 1:
        return izracunaj_vrijeme(zadatak, patkica)

    minimum = float('inf')

    pokusaj = zadatak.pop()
    for i in range(len(patkica)):
        _patkica = patkica.copy()
        patka = _patkica[i]
        del _patkica[i]
        minimum = min(minimum, max(brute_force(zadatak.copy(), _patkica), izracunaj_vrijeme([pokusaj], [patka])))

    return minimum


if __name__ == '__main__':
    n = int(input())
    programer = list(map(int, input().split()))
    tezina = list(map(int, input().split()))
    zadatak = list(zip(programer, tezina))

    patkica = list(map(int, input().split()))

    zadatak.sort(key=compare, reverse=True)
    patkica.sort(reverse=True)
    zadatak = zadatak[:20]
    patkica = patkica[:20]
    print(brute_force(zadatak, patkica))
