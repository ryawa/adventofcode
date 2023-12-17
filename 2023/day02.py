import sys

bag = {'red': 12, 'green': 13, 'blue': 14}
lines = [l.rstrip('\n').split(': ')[1] for l in sys.stdin]

possible = [True] * len(lines)
ans = 0
i = 0
while i < len(lines):
    line = lines[i]
    for turn in line.split('; '):
        if not possible[i]:
            continue
        for color in turn.split(', '):
            if not possible[i]:
                continue
            s = color.split(' ')
            if int(s[0]) > bag[s[1]]:
                possible[i] = False
    if possible[i]:
        ans += i + 1
    i += 1
print(ans)

ans = 0
for line in lines:
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    for turn in line.split('; '):
        for color in turn.split(', '):
            s = color.split(' ')
            minimums[s[1]] = max(minimums[s[1]], int(s[0]))
    ans += minimums['red'] * minimums['green'] * minimums['blue']
print(ans)
