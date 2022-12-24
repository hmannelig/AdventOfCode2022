file = open('treetop_tree_house').read().splitlines()

tree_score = 0


def is_visible(col_i, row_i) -> bool:
    return is_visible_from_top(col_i, row_i)\
           or is_visible_from_bottom(col_i, row_i)\
           or is_visible_from_left(col_i, row_i) \
           or is_visible_from_right(col_i, row_i)


def is_visible_from_top(col_i, row_i) -> bool:
    tree = grid[row_i][col_i]
    while row_i > 0:
        row_i -= 1
        if grid[row_i][col_i] >= tree:
            return False

    return True


def is_visible_from_bottom(col_i, row_i) -> bool:
    tree = grid[row_i][col_i]
    while row_i < len(grid) - 1:
        row_i += 1
        if grid[row_i][col_i] >= tree:
            return False

    return True


def is_visible_from_left(col_i, row_i) -> bool:
    tree = grid[row_i][col_i]
    while col_i > 0:
        col_i -= 1
        if grid[row_i][col_i] >= tree:
            return False

    return True


def is_visible_from_right(col_i, row_i) -> bool:
    tree = grid[row_i][col_i]
    while col_i < len(grid[row_i]) - 1:
        col_i += 1
        if grid[row_i][col_i] >= tree:
            return False

    return True


def is_edge(index: int, bottom_edge: int) -> bool:
    return index == 0 or index == bottom_edge


visible_trees_count, grid = 0, []
for line in file:
    listed_line = [int(x) for x in line]
    grid.append(listed_line)

for idx, trees_row in enumerate(grid):

    if is_edge(idx, len(grid) - 1):
        visible_trees_count += len(trees_row)

    else:
        for i, tree in enumerate(grid[idx]):

            if is_edge(i, len(grid[idx]) - 1):
                visible_trees_count += 1

            elif is_visible(i, idx):
                visible_trees_count += 1


print('First solution', visible_trees_count)