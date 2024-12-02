import sys


def part1():
    ans = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        nums = list(map(int, line.split()))
        inc = True
        if nums[1] - nums[0] < 0:
            inc = False
        prev = nums[0]
        safe = True
        for num in nums[1:]:
            if inc:
                if not 1 <= num - prev <= 3:
                    safe = False
            if not inc:
                if not 1 <= prev - num <= 3:
                    safe = False
            prev = num
        if safe:
            ans += 1
    print(ans)


def part2():
    ans = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        nums = list(map(int, line.split()))
        safe_outer = False
        for remove in range(len(nums)):
            a = nums.copy()
            a.pop(remove)
            prev = a[0]
            safe = True
            inc = True
            if a[1] - a[0] < 0:
                inc = False
            for num in a[1:]:
                if inc:
                    if not 1 <= num - prev <= 3:
                        safe = False
                if not inc:
                    if not 1 <= prev - num <= 3:
                        safe = False
                prev = num
            if safe:
                safe_outer = True
        if safe_outer:
            ans += 1
    print(ans)


part2()
