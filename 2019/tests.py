from cipher import main as cipher
from parachute import main as parachute
from keys import main as keys
from boxes import main as boxes
from modulo import main as modulo
from prime import main as prime
from fence import main as fence
from tables import main as tables
from brackets import main as brackets
from more_boxes import main as more_boxes
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


def test_parachute():
    data = [(4.2, [0.53, 0.89], 0.94),
            (2.72, [0.34, 1.53, 0.29, 0.11, 0.23], 0.65),
            (69.69, [64.09, 2.88, 0.75, 1.02, 5.14, 0.42, 3.19, 4.5, 0.54,
             2.14, 1.18, 0.14, 1.68], 0.14)]
    return test(data, parachute, "parachute")


def test_keys():
    data = [("[{", ["[/", "[\\"], 0), ("]%(", ["*[*", "]]%%(", "%+$"], 1),
            ("-}&{&*+#%", ["}}&#%%", "-%", "&{&+%", "&&&+", "}}&{&*+##%",
             "&{&*+#%", "-}{&%", "(&**+", "--&{{&**+#", "&&{{&**", "#%%",
             "--&&%%"], 4)]
    return test(data, keys, "keys")


def test_boxes():
    data = [(1, 2, 1), (10, 4, 6), (500, 125, 193)]
    return test(data, boxes, "boxes")


def test_modulo():
    data = [("31", 13), ("1111", -1), ("361542", 654213)]
    return test(data, modulo, "modulo")


def test_prime():
    data = [(3, 11), (54, 295485799), (4269, 55882399)]
    return test(data, prime, "prime")


def test_fence():
    data = [
        ([[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 0], [0, 0]], 1),
        ([[1, 1], [1, 5], [3, 5], [3, 7], [2, 7], [2, 9], [6, 9],
          [6, 7], [5, 7], [5, 3], [4, 3], [4, 4], [3, 4], [3, 2],
          [5, 2], [5, 1], [1, 1]], 6)
    ]
    return test(data, fence, "fence")


def test_tables():
    data = [([3, 2, 5], [2, 1, 4, 2, 6], [1, 1, 3, 2, 0]),
            ([3, 2, 4, 1, 5, 5, 2, 6], [4, 4, 7, 1, 1, 5], [3, 5, 0, 1, 1, 6])]
    return test(data, tables, "tables")


def test_brackets():
    data = [(3, 0, 0, 5), (2, 1, 0, 15), (2, 2, 2, 11880)]
    return test(data, brackets, "brackets")


def test_more_boxes():
    data = [(3, 2, 2), (7, 4, 1), (7070, 420, 5691)]
    return test(data, more_boxes, "more_boxes")


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
       2 - Parachute
       3 - Keys 
       4 - Boxes
       5 - Modulo
       6 - Prime
       7 - Fence
       8 - Brackets
       9 - Tables
       10 - More boxes
       11 - All the boxes
       Choose the script you want to test: """

    # TODO 5 cities
    tests = [test_cipher, test_parachute, test_keys, test_boxes,
             test_modulo, test_prime, test_fence, test_brackets, test_tables,
             test_more_boxes, test_all_the_boxes]

    while mode not in list(range(1, len(tests)+1)):
        try:
            mode = int(input(input_string.replace("\n    ", "\n")))
        except Exception:
            continue
    print()

    if tests[mode - 1]():
        print("Everything passed")


if __name__ == "__main__":
    main()
