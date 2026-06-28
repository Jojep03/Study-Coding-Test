import sys

input = sys.stdin.readline

s = input().strip()
cnt0 = 0
cnt1 = 0

if s[0] == "0":
    cnt0 += 1
else:
    cnt1 += 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == "0":
            cnt0 += 1
        else:
            cnt1 += 1
print(min(cnt0, cnt1))