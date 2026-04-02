import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    #
    # cnt = 0
    # for i in range(1, len(arr) - 1):
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             cnt += 1
    # print(arr[0], cnt)
    cnt = 0

    for i in range(2, len(arr)):
        j = i
        while j > 1 and arr[j - 1] > arr[j]:
            cnt += 1
            j -= 1
    print(arr[0], cnt)