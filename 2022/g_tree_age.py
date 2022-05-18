def main(a):
    map_ints = ["zero", "one", "two", "three", "four", "five", "six",
                "seven", "eight", "nine"]

    for i in range(len(a)):
        a[i] = map_ints.index(a[i])

    b = ''
    for j in a:
        b = int(str(b) + str(j))

    b = int(b) * 365 * 24 * 60

    return b % (10**9 + 7)


if __name__ == "__main__":
    n = int(input())
    a = input().split()
    print(main(a))
