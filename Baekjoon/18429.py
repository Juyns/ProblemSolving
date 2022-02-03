# 18429

from itertools import permutations

def calculate(n: int, k: int, kits: list):
    combs = list(permutations(kits, len(kits)))
    result = 0
    for lst in combs:
        current = 0
        for i in range(n):
            current = current + lst[i] - k
            if current < 0: break
        if current >= 0:
            result += 1
    return result

n, k = map(int, input().split())
kits = list(map(int, input().split()))

print(calculate(n, k, kits))