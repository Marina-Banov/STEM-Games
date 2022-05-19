import math


def main(y1, y2, a):
    # if y2 == 1:
    #     return -1

    vel = math.sqrt((y1-y2)**2 + 1)
    _a = -math.pi / 2
    # _a = math.atan2(y2-y1, 1)
    a = a * math.pi / 180
    h = y2
    count = 0
    # print()
    while h >= 1:
        vel_y = vel * math.sin(_a)
        # print(vel_y, h, _a*180/math.pi)
        _a += a
        count += 1
        if _a >= 0:
            return count
        h -= abs(vel_y)
    return -1

    # count = math.ceil(-_a / a)

    # return count if count*(y1-y2) > 0 else -1


if __name__ == "__main__":
    y1 = int(input())
    y2 = int(input())
    a = int(input())
    print(main(y1, y2, a))
