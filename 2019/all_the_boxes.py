def row_start_odd(n):
    meta_step = 7
    arr = [1, 2, 4]
    if n <= 3:
        return arr[n-1], meta_step

    prev = 4
    step = 4
    inc = True
    for i in range(3, n):
        if inc:
            meta_step += 4
        prev += step
        inc = not inc
        if inc:
            step += 2

    return prev, meta_step


def row_start_even(n):
    prev = 5 if n % 2 else 7
    step = 8 if n % 2 else 10
    meta_step = 7
    for i in range(int(n/2)-1):
        prev += step
        step += 4
        meta_step += 4
    return prev, meta_step


def f(init, step, m):
    res = init
    stop = int(m/2)
    if m % 2 == 0:
        step += 2
        stop -= 1
    for i in range(stop):
        res += step
        step += 4
    return res


def first_row(m):
    prev = 1
    step = 2
    for i in range(m-1):
        prev += step
        step += 1
    return prev


def main(n, m):
    if n == 1:
        return first_row(m)
    init, step = row_start_odd(n) if m % 2 else row_start_even(n)
    return f(init, step, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))
