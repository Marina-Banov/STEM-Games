def max_hist(row):
    result = []
    max_area = 0
    i = 0

    while i < len(row):
        if len(result) == 0 or row[result[-1]] <= row[i]:
            result.append(i)
            i += 1
        else:
            top_val = row[result.pop()]
            area = top_val * i
            if len(result):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)

    while len(result):
        top_val = row[result.pop()]
        area = top_val * i
        if len(result):
            area = top_val * (i - result[-1] - 1)
        max_area = max(area, max_area)

    return max_area


def max_rectangle(A):
    result = max_hist(A[0])

    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if A[i][j]:
                A[i][j] += A[i-1][j]
        result = max(result, max_hist(A[i]))

    return result


def main(_grid):
    grid = [[0 for _ in range(len(_grid))] for _ in range(len(_grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if _grid[i][j] == '.':
                grid[i][j] = 1
    return max_rectangle(grid)


if __name__ == "__main__":
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(input().strip()))
    print(main(grid))
