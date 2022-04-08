def main(r, islands):
    return 1 - round(sum([i*i for i in islands]) / (r*r), 2)


if __name__ == "__main__":
    r, m = map(float, input().split())
    islands = []
    for i in range(int(m)):
        islands.append(float(input()))
    print(main(r, islands))
