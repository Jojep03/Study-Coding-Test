# [BOJ 1806] 부분합 - Python

## 문제 설명

길이가 `N`인 수열이 주어진다.
이때 연속된 수들의 부분합 중에서 그 합이 `S` 이상이 되는 것들 중, 가장 짧은 길이를 구하는 문제이다.

만약 합이 `S` 이상이 되는 연속 부분 수열이 없다면 `0`을 출력한다.

## 문제 풀이

이 문제는 **투 포인터**를 이용해서 풀 수 있다.

`left`와 `right`를 사용해서 현재 보고 있는 연속 구간을 정한다.

현재 구간의 합을 `res`라고 했을 때,

* `res >= S`이면 조건을 만족하므로 현재 구간의 길이를 정답 후보로 갱신한다.
* 이후 더 짧은 구간을 찾기 위해 왼쪽 값을 빼고 `left`를 오른쪽으로 이동한다.
* `res < S`이면 합이 부족하므로 `right`를 오른쪽으로 이동하면서 구간을 늘린다.

정답을 저장하는 `cnt`는 처음에 `n + 1`로 설정한다.
가능한 최대 길이는 `n`이기 때문에, 마지막까지 `cnt`가 `n + 1`이면 조건을 만족하는 구간이 없다는 뜻이다.

## 코드

```python
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = 0
res = lst[0]
cnt = n + 1

while left <= right:
    if res >= s:
        cnt = min(cnt, right - left + 1)
        res -= lst[left]
        left += 1
    else:
        right += 1
        if right < n:
            res += lst[right]
        else:
            break

print(0 if cnt == n + 1 else cnt)
```

## 핵심 포인트

```python
if res >= s:
```

현재 구간의 합이 `S` 이상이면 조건을 만족하므로 최소 길이를 갱신한다.

```python
cnt = min(cnt, right - left + 1)
```

현재 구간의 길이는 `right - left + 1`이다.

```python
res -= lst[left]
left += 1
```

왼쪽 값을 먼저 빼고 `left`를 이동해야 한다.
`left`를 먼저 증가시키면 원래 빠져야 할 값이 아니라 다음 값이 빠지게 된다.

```python
print(0 if cnt == n + 1 else cnt)
```

끝까지 `cnt`가 갱신되지 않았다면 조건을 만족하는 부분합이 없다는 뜻이므로 `0`을 출력한다.

## 시간 복잡도

투 포인터 방식에서는 `left`와 `right`가 각각 최대 `N`번만 이동한다.

따라서 시간 복잡도는

```text
O(N)
```

이다.
