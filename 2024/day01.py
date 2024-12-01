import sys


def part1():
    a = []
    b = []

    for line in sys.stdin:
        if line == "\n":
            break
        line = list(map(int, line.rstrip().split("   ")))
        a.append(line[0])
        b.append(line[1])

    a.sort()
    b.sort()
    print(sum([abs(x - y) for x, y in zip(a, b)]))


def part2():
    a = []
    b = []
    occurrences = {}

    for line in sys.stdin:
        if line == "\n":
            break
        line = list(map(int, line.rstrip().split("   ")))
        a.append(line[0])
        occurrences[line[1]] = occurrences.setdefault(line[1], 0) + 1

    ans = 0
    for x in a:
        ans += x * occurrences.setdefault(x, 0)
    print(ans)


part2()
