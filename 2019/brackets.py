from itertools import permutations


def main(a, b, c):
    _sum = sum([a, b, c])
    assert _sum > 0
    if _sum < 2:
        return _sum

    num = 0
    seen = {}
    bracket_permutation = permutations([1, 2] * a + [3, 4] * b + [5, 6] * c)

    for brackets in bracket_permutation:
        if brackets[0] % 2 == 0:
            continue
        bracket_str = ''.join(str(n) for n in brackets)
        if bracket_str in seen:
            continue

        current_bracket = []
        correct = True
        for i in range(len(brackets)):
            if brackets[i] % 2 == 0:
                if len(current_bracket) < 1 or brackets[i] - current_bracket.pop() != 1:
                    correct = False
                    break
            else:
                current_bracket.append(brackets[i])
        if correct and len(current_bracket) == 0:
            seen[bracket_str] = 1
            num += 1
    return num


if __name__ == "__main__":
    print(main(2, 2, 2))
