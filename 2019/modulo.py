from itertools import permutations


def main(n):
    list_n = list(set(permutations(list(n))))
    list_n.sort(reverse=True)
    for i in list_n:
        n = int("".join(i))
        if n % 8 == 5:
            return n
    return -1


if __name__ == "__main__":
    print(main(input()))
