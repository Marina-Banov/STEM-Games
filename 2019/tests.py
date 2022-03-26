import cipher
import modulo
import all_the_boxes


def test_cipher():
    data = [
        ("kszqcas hc ghsa uoasg hsqvbczcum ofsbo", "welcome to stem games technology arena"),
    ]

    for i, t in enumerate(data):
        sa, assert_res = t
        res = cipher.main(sa)
        e = f"cipher({sa}) == {res} --- Should be {assert_res}"
        try:
            assert assert_res == res, e
            # print(f"Passed {i+1} tests")
        except Exception as e:
            print(e)
            return False
    return True


def test_modulo():
    data = [("31", 13), ("1111", -1), ("361542", 654213)]

    for i, t in enumerate(data):
        n, assert_res = t
        res = modulo.main(n)
        e = f"modulo({n}) == {res} --- Should be {assert_res}"
        try:
            assert assert_res == res, e
            # print(f"Passed {i+1} tests")
        except Exception as e:
            print(e)
            return False
    return True


def test_all_the_boxes():
    data = [
        (1, 7, 28), (1, 8, 36), (2, 7, 35), (2, 8, 46), (3, 7, 37),
        (3, 8, 44), (4, 7, 53), (4, 8, 68), (5, 7, 57), (5, 8, 64),
        (14, 15, 399), (14, 16, 442), (15, 15, 413), (15, 16, 428),
        (1, 1, 1), (1, 3, 6), (4, 1, 8),
    ]

    for i, t in enumerate(data):
        n, m, assert_res = t
        res = all_the_boxes.main(n, m)
        e = f"all_the_boxes({n}, {m}) == {res} --- Should be {assert_res}"
        try:
            assert assert_res == res, e
            # print(f"Passed {i+1} tests")
        except Exception as e:
            print(e)
            return False
    return True


if __name__ == "__main__":
    mode = 0
    input_string = """\n   1 - Cipher
       2 - Modulo
       3 - All the boxes
       Choose the script you want to test: """
    while mode not in list(range(1,4)):
        try:
            mode = int(input(input_string.replace("\n    ", "\n")))
        except Exception as e:
            continue
    print()
    if mode == 1:
        res = test_cipher()
    elif mode == 2:
        res = test_modulo()
    elif mode == 3:
        res = test_all_the_boxes()
    if res:
        print("Everything passed")
