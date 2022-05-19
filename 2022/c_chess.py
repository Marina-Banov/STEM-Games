def get_clean_board():
    return [[0 for _ in range(8)] for _ in range(8)]


def legal_move(x, y):
    return not (x < 0 or y < 0 or x > 7 or y > 7)


knight_moves = [
    [-2, -1], [-2, 1], [2, -1], [2, 1],
    [1, 2], [-1, 2], [1, -2], [-1, -2]
]
possible_answers = ["knight", "bishop", "rook", "queen", "impossible"]


def knight(is_attacking, i, j):
    for move in knight_moves:
        if legal_move(i + move[0], j + move[1]):
            is_attacking[i + move[0]][j + move[1]] += 1


def rook(board, is_attacking, i, j):
    _i = i - 1
    while _i >= 0:
        is_attacking[_i][j] += 1
        if board[_i][j] == '#':
            break
        _i -= 1

    _i = i + 1
    while _i < 8:
        is_attacking[_i][j] += 1
        if board[_i][j] == '#':
            break
        _i += 1

    _j = j - 1
    while _j >= 0:
        is_attacking[i][_j] += 1
        if board[i][_j] == '#':
            break
        _j -= 1

    _j = j + 1
    while _j < 8:
        is_attacking[i][_j] += 1
        if board[i][_j] == '#':
            break
        _j += 1


def bishop_move(board, is_attacking, i, j, i_ch, j_ch):
    i += i_ch
    j += j_ch
    while legal_move(i, j):
        is_attacking[i][j] += 1
        if board[i][j] == '#':
            return
        i += i_ch
        j += j_ch


def bishop(board, is_attacking, i, j):
    bishop_move(board, is_attacking, i, j, 1, 1)
    bishop_move(board, is_attacking, i, j, -1, 1)
    bishop_move(board, is_attacking, i, j, 1, -1)
    bishop_move(board, is_attacking, i, j, -1, -1)


def queen(board, is_attacking, i, j):
    rook(board, is_attacking, i, j)
    bishop(board, is_attacking, i, j)


def attacker(is_attacking, figurice_poz):
    for i, j in figurice_poz:
        if is_attacking[i][j] == 0:
            return False
    return True


def check_figure(board, under_attack, i, j):
    is_attacking = get_clean_board()
    knight(is_attacking, i, j)
    if attacker(is_attacking, under_attack):
        return 0

    is_attacking = get_clean_board()
    bishop(board, is_attacking, i, j)
    if attacker(is_attacking, under_attack):
        return 1

    is_attacking = get_clean_board()
    rook(board, is_attacking, i, j)
    if attacker(is_attacking, under_attack):
        return 2

    is_attacking = get_clean_board()
    queen(board, is_attacking, i, j)
    if attacker(is_attacking, under_attack):
        return 3

    return 4


def main(board):
    is_attacking = get_clean_board()
    under_attack = []

    for i in range(8):
        for j in range(8):
            if board[i][j] == '.':
                continue
            under_attack.append((i, j))
            knight(is_attacking, i, j)
            queen(board, is_attacking, i, j)

    ans = 4
    for i in range(8):
        for j in range(8):
            if is_attacking[i][j] < len(under_attack):
                continue
            rj = check_figure(board, under_attack, i, j)
            if rj < ans:
                ans = rj
    return possible_answers[ans]


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        board = []
        for _ in range(8):
            board.append(input())
        print(main(board))
        if i < n - 1:
            input()
