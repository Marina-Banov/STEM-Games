import math


def is_prime(n):
    limit = int(math.sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True


def find_next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


def lucas_number(n):
    a = 2
    b = 1
    for i in range(n-1):
        tmp = b
        b += a
        a = tmp
    return b


def main(n):
    return lucas_number(find_next_prime(n)) % 1000000000


if __name__ == "__main__":
    print(main(int(input())))
