import sys

input = sys.stdin.readline

alpha = input().rstrip()

cnt = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

for al in alpha:
    cnt[al.upper()] += 1

max_val = max(cnt.values())

result = [k for k, v in cnt.items() if v == max_val]
if len(result) > 1:
    print("?")
else:
    print(result[0])