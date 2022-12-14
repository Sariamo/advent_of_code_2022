def is_visible(forest, i, j):
    left_view = True
    right_view = True
    top_view = True
    bottom_view = True

    for left in range(0, i):
        if forest[left][j] >= forest[i][j]:
            left_view = False
            break
    for right in range(i + 1, len(forest)):
        if forest[right][j] >= forest[i][j]:
            right_view = False
            break
    for top in range(0, j):
        if forest[i][top] >= forest[i][j]:
            top_view = False
            break
    for bottom in range(j + 1, len(forest[i])):
        if forest[i][bottom] >= forest[i][j]:
            bottom_view = False
            break
    return left_view or right_view or top_view or bottom_view


forest = []
with open("input", "r") as d:
    for inp in d.readlines():
        tress_row = []
        for tree in inp:
            if tree != "\n":
                tress_row.append(tree)
        forest.append(tress_row)

visible_ctr = 0

for i, trees_row in enumerate(forest):
    visible_row = []
    for j, tree in enumerate(trees_row):
        if is_visible(forest, i, j):
            visible_ctr += 1

print(visible_ctr)
