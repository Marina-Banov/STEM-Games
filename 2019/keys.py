def edit_distance(a, b):
    edit = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        edit[i][0] = i
    for j in range(1, len(b) + 1):
        edit[0][j] = j
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                edit[i][j] = min(edit[i][j-1]+1,
                                 edit[i-1][j]+1,
                                 edit[i-1][j-1])
            else:
                edit[i][j] = min(edit[i][j-1]+1,
                                 edit[i-1][j]+1,
                                 edit[i-1][j-1]+1)
    return edit[len(a)][len(b)]


def main(query, target):
    res = []
    for i in range(len(target)):
        res.append((i, edit_distance(query, target[i])))
    res.sort(key=lambda t: t[1])
    # print(res)
    return res[0][0]


if __name__ == "__main__":
    n, query = input().split()
    target = []
    for i in range(int(n)):
        target.append(input().strip())
    print(main(query, target))
