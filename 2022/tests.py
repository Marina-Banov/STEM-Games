from d_spam import main as d_spam
from h_farm import main as h_farm
from i_ribbons import main as i_ribbons
from j_migrations import main as j_migrations


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


def test_d_spam():
    data = [("ssppamam", 2), ("spspaxaaspmmmmm", 2), ("amspamspm", 1)]
    return test(data, d_spam, "d_spam")


def test_h_farm():
    data = [(["##.#", "...#", "....", ".###"], 6)]
    return test(data, h_farm, "h_farm")


def test_i_ribbons():
    data = [(3, 5, 2), (5, 3, 4), (1, 1, 0), (6, 3, 3), (5, 4, 4), (6, 4, 4)]
    return test(data, i_ribbons, "i_ribbons")


def test_j_migrations():
    data = [(10000, 5, [100, 1200], 50)]
    return test(data, j_migrations, "j_migrations")


def main():
    mode = 0
    input_string = """\n   1 - D Spam
       2 - H Farm
       3 - I Ribbons
       4 - J Migrations
       Choose the script you want to test: """

    tests = [test_d_spam, test_h_farm, test_i_ribbons, test_j_migrations]

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
