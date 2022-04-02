from cipher import main as cipher
from boxes import main as boxes
from modulo import main as modulo
from fence import main as fence
from brackets import main as brackets
from all_the_boxes import main as all_the_boxes


def test(data, f, name):
    for i, t in enumerate(data):
        *var, assert_res = t
        res = f(*var)
        e = f"{name}{tuple(var)} == {res} --- Should be {assert_res}"
        try:
            assert assert_res == res, e
            # print(f"Passed {i+1} tests")
        except Exception as e:
            print(e)
            return False
    return True


def test_cipher():
    data = [
        ("kszqcas hc ghsa uoasg hsqvbczcum ofsbo",
         "welcome to stem games technology arena"),
    ]
    return test(data, cipher, "cipher")


def test_boxes():
    data = [(1, 2, 1), (10, 4, 6), (500, 125, 193)]
    return test(data, boxes, "boxes")


def test_modulo():
    data = [("31", 13), ("1111", -1), ("361542", 654213)]
    return test(data, modulo, "modulo")


def test_fence():
    data = [
        ([[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 0], [0, 0]], 1),
        ([[1, 1], [1, 5], [3, 5], [3, 7], [2, 7], [2, 9], [6, 9],
          [6, 7], [5, 7], [5, 3], [4, 3], [4, 4], [3, 4], [3, 2],
          [5, 2], [5, 1], [1, 1]], 6)
    ]
    return test(data, fence, "fence")


def test_brackets():
    data = [(3, 0, 0, 5), (2, 1, 0, 15), (2, 2, 2, 11880)]
    return test(data, brackets, "brackets")


def test_all_the_boxes():
    data = [
        (1, 7, 28), (1, 8, 36), (2, 7, 35), (2, 8, 46), (3, 7, 37),
        (3, 8, 44), (4, 7, 53), (4, 8, 68), (5, 7, 57), (5, 8, 64),
        (14, 15, 399), (14, 16, 442), (15, 15, 413), (15, 16, 428),
        (1, 1, 1), (1, 3, 6), (4, 1, 8),
    ]
    return test(data, all_the_boxes, "all_the_boxes")


def main():
    mode = 0
    input_string = """\n   1 - Cipher
       2 - Boxes
       3 - Modulo
       4 - Fence
       5 - Brackets
       6 - All the boxes
       Choose the script you want to test: """

    while mode not in list(range(1, 7)):
        try:
            mode = int(input(input_string.replace("\n    ", "\n")))
        except Exception:
            continue
    print()

    if mode == 1:
        res = test_cipher()
    elif mode == 2:
        res = test_boxes()
    elif mode == 3:
        res = test_modulo()
    elif mode == 4:
        res = test_fence()
    elif mode == 5:
        res = test_brackets()
    elif mode == 6:
        res = test_all_the_boxes()
    else:
        res = False
    if res:
        print("Everything passed")


if __name__ == "__main__":
    main()
