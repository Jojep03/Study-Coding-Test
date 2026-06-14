import sys

input = sys.stdin.readline

x = input().strip()
cnt = {i.upper(): 0 for i in x}
for i in x:
    i = i.upper()
    cnt[i] += 1

max_cnt = max(cnt.values())
res = 0
answer = ''
for ch in cnt:
    if cnt[ch] == max_cnt:
        res += 1
        answer = ch
print("?" if res > 1 else answer)
