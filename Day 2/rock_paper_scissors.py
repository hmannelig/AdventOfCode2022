f = open("rock_paper_scissors_input").read().splitlines()


def is_win(moves) -> bool:
    winning_moves = {
        "X": ["C"],
        "Y": ["A"],
        "Z": ["B"],
    }
    return moves.__getitem__(0) in winning_moves.get(moves.__getitem__(1))


def is_draw(moves) -> bool:
    draw_moves = {
        "X": ["A"],
        "Y": ["B"],
        "Z": ["C"],
    }
    return moves.__getitem__(0) in draw_moves.get(moves.__getitem__(1))


def is_lose(moves) -> bool:
    lose_moves = {
        "X": ["B"],
        "Y": ["C"],
        "Z": ["A"],
    }
    return moves.__getitem__(0) in lose_moves.get(moves.__getitem__(1))


def get_move_score(move) -> int:
    moves_list = ["X", "Y", "Z"]
    return moves_list.index(move) + 1


def get_first_part_points(moves_list) -> int:
    round_result = 0

    if is_win(split_line):
        round_result += get_move_score(moves_list.__getitem__(1)) + 6

    elif is_draw(split_line):
        round_result += get_move_score(moves_list.__getitem__(1)) + 3

    elif is_lose(split_line):
        round_result += get_move_score(moves_list.__getitem__(1))

    return round_result


def get_winning_move(move) -> str:
    winning_moves = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }
    return winning_moves.get(move)


def get_drawing_move(move) -> str:
    draw_moves = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }
    return draw_moves.get(move)


def get_losing_move(move) -> str:
    lose_moves = {
        "A": "Z",
        "B": "X",
        "C": "Y",
    }
    return lose_moves.get(move)


def get_second_part_points(moves_list) -> int:
    round_result = 0

    if moves_list.__getitem__(1) == "Z":
        needed_move = get_winning_move(moves_list.__getitem__(0))
        round_result += get_move_score(needed_move) + 6

    elif moves_list.__getitem__(1) == "Y":
        needed_move = get_drawing_move(moves_list.__getitem__(0))
        round_result += get_move_score(needed_move) + 3

    elif moves_list.__getitem__(1) == "X":
        needed_move = get_losing_move(moves_list.__getitem__(0))
        round_result += get_move_score(needed_move)

    return round_result


first_part_score = second_part_score = 0
for line in f:
    split_line = line.split(" ")

    first_part_score += get_first_part_points(split_line)
    second_part_score += get_second_part_points(split_line)

print(">> Score (Part I): ", first_part_score)
print(">> Score (Part II): ", second_part_score)
