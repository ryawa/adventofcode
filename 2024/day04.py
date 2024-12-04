import sys


def part1():
    grid = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        grid.append([c for c in line] + ["."] * 4)
    l = len(grid[0])
    for i in range(4):
        grid.append(["."] * l)

    needles = ["XMAS", "SAMX"]
    horiz = [[0, 0], [1, 0], [2, 0], [3, 0]]
    vert = [[0, 0], [0, 1], [0, 2], [0, 3]]
    diag1 = [[0, 0], [1, 1], [2, 2], [3, 3]]
    diag2 = [[3, 0], [2, 1], [1, 2], [0, 3]]
    lines = [horiz, vert, diag1, diag2]
    ans = 0
    for i in range(len(grid) - 3):
        for j in range(len(grid[i]) - 3):
            for line in lines:
                for needle in needles:
                    found = True
                    for offset, c in zip(line, needle):
                        if grid[j + offset[0]][i + offset[1]] != c:
                            found = False
                    if found:
                        ans += 1
    print(ans)


def part2():
    grid = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        grid.append([c for c in line])

    possible = [
        [
            ["M", ".", "S"],
            [".", "A", "."],
            ["M", ".", "S"],
        ],
        [
            ["M", ".", "M"],
            [".", "A", "."],
            ["S", ".", "S"],
        ],
        [
            ["S", ".", "S"],
            [".", "A", "."],
            ["M", ".", "M"],
        ],
        [
            ["S", ".", "M"],
            [".", "A", "."],
            ["S", ".", "M"],
        ],
    ]

    ans = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[i]) - 2):
            for p in possible:
                found = True
                for x in range(3):
                    for y in range(3):
                        if p[x][y] == ".":
                            continue
                        if grid[j + x][i + y] != p[x][y]:
                            found = False
                if found:
                    ans += 1
                    break
    print(ans)


part2()
