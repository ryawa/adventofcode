import itertools
import sys

lines = ['.' + l.rstrip('\n') + '.\n' for l in sys.stdin]
hborder = '.' * len(lines[0])
lines.insert(0, hborder)
lines.append(hborder)

ans = 0
i = 1
gears = {}
while i < len(lines) - 1:
    num = ''
    adjacent = False
    star = -1
    j = 1
    while j < len(lines[i]) - 1:
        c = lines[i][j]
        if c.isdigit():
            if not adjacent:
                for d in itertools.product(range(-1, 2), repeat=2):
                    ac = lines[i + d[0]][j + d[1]]
                    if not ac.isalnum() and ac != '.':
                        if star == -1 and ac == '*':
                            star = (i + d[0]) * len(lines[0]) + j + d[1]
                        adjacent = True
            num += c
        elif num != '':
            if adjacent:
                ans += int(num)
                if star != -1:
                    if star not in gears:
                        gears[star] = [int(num)]
                    else:
                        gears[star].append(int(num))
                    star = -1
                adjacent = False
            num = ''
        j += 1
    i += 1
print(ans)

ans = 0
for gear in gears.values():
    if len(gear) != 2:
        continue
    ans += gear[0] * gear[1]
print(ans)
