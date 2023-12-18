import sys

lines = [l.rstrip('\n').split(': ')[1] for l in sys.stdin]
counts = [1] * len(lines)

ans = 0
for idx, line in enumerate(lines):
    card = line.split(' | ')
    winning = {num for num in card[0].split(' ') if num}
    own = {num for num in card[1].split(' ') if num}
    won = len(winning & own)
    if won:
        ans += 2 ** (won - 1)
        for i in range(idx + 1, idx + won + 1):
            counts[i] += counts[idx]


print(ans)
print(sum(counts))
