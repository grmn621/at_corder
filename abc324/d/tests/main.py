from collections import Counter
from math import isqrt

N = int(input())
S = input().strip()

# Count the frequency of each digit in S
freq = Counter(S)

# Generate all possible permutations of S
perms = []
def generate_permutations(s, count):
    if len(s) == N:
        perms.append(s)
        return
    for digit in count:
        if count[digit] > 0:
            count[digit] -= 1
            generate_permutations(s + digit, count)
            count[digit] += 1
generate_permutations("", freq)

# Count the number of permutations that are square numbers
count = 0
for perm in perms:
    num = int(perm)
    root = isqrt(num)
    if root * root == num:
        count += 1

print(count)