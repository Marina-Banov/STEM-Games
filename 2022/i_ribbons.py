def main(n, m):
    if m % n == 0:
        return 0
    _i = set(range(0, n*m, m))
    _f = set(range(0, n*m, n)).intersection(_i)
    return len(_i) - len(_f)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))
