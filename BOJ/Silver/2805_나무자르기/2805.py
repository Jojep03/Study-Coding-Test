import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for tree in trees:
        if (tree - mid) > 0:
            cnt += (tree - mid)

    if cnt >= m:
        start = mid + 1
        answer = mid

    else:
        end = mid - 1

print(answer)