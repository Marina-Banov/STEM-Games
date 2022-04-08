from itertools import permutations
# import time


def recursion(brackets, stack):
    _sum = sum(brackets)
    assert _sum >= 0
    if _sum == 0:
        return 1

    _num = 0
    for i in range(6):
        if brackets[i] < 1:
            continue
        if i % 2 != 0:
            if not stack:
                continue
            if i - stack[-1] != 1:
                continue
            _num += recursion(brackets[:i] + [brackets[i] - 1] + brackets[i+1:], stack[:-1])
        else:
            tmp = stack.copy()
            tmp.append(i)
            _num += recursion(brackets[:i] + [brackets[i] - 1] + brackets[i+1:], tmp)

    return _num


def iteration(a, b, c):
    _sum = sum([a, b, c])
    assert _sum > 0
    if _sum < 2:
        return _sum

    # this is bottleneck :(
    bracket_permutation = permutations([1, 2] * a + [3, 4] * b + [5, 6] * c)
    bracket_permutation = set(bracket_permutation)
    num = len(bracket_permutation)
    # print(len(bracket_permutation))

    for brackets in bracket_permutation:
        if brackets[0] % 2 == 0:
            num -= 1
            continue

        current_bracket = []
        for i in range(len(brackets)):
            if brackets[i] % 2 == 0:
                if len(current_bracket) < 1 or brackets[i] - current_bracket.pop() != 1:
                    num -= 1
                    break
            else:
                current_bracket.append(brackets[i])
    return num


def main(a, b, c, r=True):
    if r:
        return recursion([a, a, b, b, c, c], [])
    else:
        return iteration(a, b, c)


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    # start = time.time()
    # print(main(a, b, c, False))
    # end = time.time()
    # print(end - start)
    # start = time.time()
    print(main(a, b, c))
    # end = time.time()
    # print(end - start)
