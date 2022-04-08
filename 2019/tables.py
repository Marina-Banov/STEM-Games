def main(tables, teams):
    res = [0] * len(teams)
    for i in range(len(teams)):
        for j in range(len(tables)):
            if tables[j] >= teams[i]:
                tables[j] -= teams[i]
                res[i] = j+1
                break
    return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    tables = list(map(int, input().split()))
    teams = list(map(int, input().split()))
    print(main(tables, teams))
