import sys

lines = [l.rstrip('\n') for l in sys.stdin]

ans = 0
for line in lines:
    for c in line:
        if c.isdigit():
            ans += int(c) * 10
            break
    for c in reversed(line):
        if c.isdigit():
            ans += int(c)
            break
print(ans)

ans = 0
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
for line in lines:
    found = []
    i = 0
    while i < len(line):
        c = line[i]
        if c.isdigit():
            found.append(int(c))
        else:
            word = c
            j = 1
            while True:
                possible = [k for k in numbers if k.startswith(word)]
                if not possible:
                    break
                if possible[0] == word:
                    found.append(numbers[word])
                    break
                if i + j > len(line) - 1:
                    break
                word += line[i + j]
                j += 1
        i += 1
    ans += found[0] * 10 + found[-1]
print(ans)
