def main(m, n):
    boxes = [True for i in range(m)]

    for i in range(2, n+1):
        if i % 2:
            boxes = [not el if (idx + 1) % i == 0 else el for idx, el in enumerate(boxes)]
        else:
            boxes = [not el if (len(boxes) - idx) % i == 0 else el for idx, el in enumerate(boxes)]

    return boxes.count(True)


if __name__ == "__main__":
    m, n = list(map(int, input().split()))
    print(main(m, n))
