from itertools import permutations


def main(n):
    list_n = set(permutations(list(n)))
    res = []
    for i in list_n:
        n = 0
        for c in i:
            n = n*10 + int(c)
        if n % 8 == 5:
            res.append(n)
    return max(res) if len(res) > 0 else -1


if __name__ == "__main__":
    print(main(input()))
