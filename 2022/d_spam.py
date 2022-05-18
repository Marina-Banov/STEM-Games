def main(st):
    s, p, a, m = 0, 0, 0, 0
    for c in st:
        if c == "s":
            s += 1
        elif c == "p" and s > 0:
            s -= 1
            p += 1
        elif c == "a" and p > 0:
            p -= 1
            a += 1
        elif c == "m" and a > 0:
            a -= 1
            m += 1
    return m


if __name__ == "__main__":
    n = input()
    print(main(input()))
