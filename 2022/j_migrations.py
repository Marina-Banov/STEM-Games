def main(n, x, g):
    _sum = sum(g)
    p = _sum / n
    z = 0
    _n = n
    for i in range(x):
        f = _n * p
        z += f
        _n -= f
    return int(z / n * 100)


if __name__ == "__main__":
    n = int(input())
    m = input()
    x = int(input())
    g = map(int, input().split())
    print(main(n, x, g))
