# [Silver III] 블로그 - 21921

[문제 링크](https://www.acmicpc.net/problem/21921)

## 문제 설명

N일 동안의 방문자 수가 주어지고, X일 동안 가장 많이 들어온 방문자 수를 구하는 문제이다.

연속된 X일 동안의 방문자 수 합 중 최댓값을 구하고, 그 최댓값이 몇 번 나오는지도 함께 출력해야 한다.

단, 최대 방문자 수가 0명이라면 `SAD`를 출력한다.

## 입력

첫째 줄에 블로그를 시작하고 지난 일수 `N`과 기간 `X`가 주어진다.

둘째 줄에 `N`일 동안의 방문자 수가 공백으로 구분되어 주어진다.

## 출력

최대 방문자 수가 0이라면 `SAD`를 출력한다.

그렇지 않다면 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력하고, 둘째 줄에 그 기간이 몇 개 있는지 출력한다.

## 풀이 아이디어

처음 X일 동안의 방문자 수 합을 먼저 구한다.

그다음 하루씩 오른쪽으로 이동하면서 새로 포함되는 값을 더하고, 빠지는 값을 빼면 된다.

이 방식을 슬라이딩 윈도우라고 한다.

예를 들어 X가 3일 때,

```text
[1, 2, 3] 4 5
```

처음 합은 `1 + 2 + 3`이다.

다음 구간은

```text
1 [2, 3, 4] 5
```

이므로 기존 합에서 `1`을 빼고 `4`를 더하면 된다.

즉, 매번 구간 합을 새로 구하지 않아도 된다.

## 코드

```python
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")
    exit(0)

cnt = sum(visitors[:x])
res = cnt
max_cnt = 1

for i in range(x, n):
    cnt += visitors[i]
    cnt -= visitors[i - x]

    if cnt > res:
        res = cnt
        max_cnt = 1
    elif cnt == res:
        max_cnt += 1

print(res)
print(max_cnt)
```

## 코드 설명

```python
cnt = sum(visitors[:x])
res = cnt
max_cnt = 1
```

처음 X일 동안의 방문자 수 합을 구한다.

이 값을 현재 최대 방문자 수 `res`로 저장하고, 최대값이 나온 횟수를 `1`로 설정한다.

```python
for i in range(x, n):
    cnt += visitors[i]
    cnt -= visitors[i - x]
```

구간을 오른쪽으로 한 칸씩 이동한다.

새롭게 포함되는 방문자 수 `visitors[i]`를 더하고, 기존 구간에서 빠지는 방문자 수 `visitors[i - x]`를 뺀다.

```python
if cnt > res:
    res = cnt
    max_cnt = 1
```

현재 구간의 방문자 수가 기존 최대값보다 크다면 최대값을 갱신한다.

새로운 최대값이 등장한 것이므로 개수는 다시 `1`로 초기화한다.

```python
elif cnt == res:
    max_cnt += 1
```

현재 구간의 방문자 수가 기존 최대값과 같다면 최대값이 나온 횟수를 1 증가시킨다.

## 시간복잡도

처음 구간 합을 구하는 데 `O(X)`가 걸린다.

이후 나머지 구간을 한 번씩만 확인하므로 `O(N)`이 걸린다.

따라서 전체 시간복잡도는 `O(N)`이다.

## 정리

이 문제는 연속된 X일 동안의 합을 구해야 하므로 슬라이딩 윈도우를 사용하면 된다.

매번 `sum()`으로 구간 합을 다시 계산하면 시간이 오래 걸릴 수 있다.

이전 구간 합에서 빠지는 값은 빼고, 새로 들어오는 값은 더하는 방식으로 효율적으로 해결할 수 있다.
