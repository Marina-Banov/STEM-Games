def main(m, n):
    boxes = list(range(m))
    i = n-1
    while len(boxes) > 1:
        boxes.pop(i)
        i = (i + n-1) % len(boxes)
    return boxes[0]


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(main(m, n))
