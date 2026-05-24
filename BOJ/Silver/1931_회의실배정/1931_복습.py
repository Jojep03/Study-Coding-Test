import sys

input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    st, en = map(int, input().split())
    times.append((st, en))

times.sort(key=lambda x: (x[1], x[0]))

res = 1
first = times[0][1]
for start, end in times[1:]:
    if start >= first:
        res += 1
        first = end
print(res)