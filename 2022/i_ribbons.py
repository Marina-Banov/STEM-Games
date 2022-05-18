def main(n, m):
    if m % n == 0:
        return 0
    i = 0
    c = 0
    # print()
    while i < n*m:
        i += m
        if i % n:
            # print(i)
            c += 1
    return c


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))
