import math


def main(h, h2, d):
    angle = 90 - math.degrees(math.atan(h - h2))
    new_angle = angle
    height = h2
    new_height = height
    count = 0

    if angle >= 90:
      print(0)
    elif height <= 1 or h <= 1:
      print(-1)

    while new_height >= 1 and height > 1:
      count += 1
      height = new_height
      new_angle += d
      new_height = height - math.tan(math.radians(new_angle))
      if new_height < 1 and new_angle < 90:
        return -1
      if new_angle >= 90:
        return count


if __name__ == "__main__":
    h = int(input())
    h2 = int(input())
    d = int(input())
    print(main(h, h2, d))
