import re
import sys


def part1():
    ans = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        res = re.findall(r"mul\((\d+),(\d+)\)", line)
        for mul in res:
            n1, n2 = map(int, mul)
            ans += n1 * n2
    print(ans)


def part2():
    ans = 0
    do = True
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        res = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for op in res:
            if op == "do()":
                do = True
                continue
            if op == "don't()":
                do = False
                continue
            if do:
                p1, p2 = op.split(",")
                n1 = int(p1[4:])
                n2 = int(p2[:-1])
                ans += n1 * n2
    print(ans)


part2()
