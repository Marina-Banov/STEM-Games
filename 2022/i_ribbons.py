from math import gcd


def main(n, m):
    if m % n == 0:
        return 0
    return n - gcd(n, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))
