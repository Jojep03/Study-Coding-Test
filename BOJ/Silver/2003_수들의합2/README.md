# [BOJ 2003] 수들의 합 2 - Python

## 문제 설명

길이가 `N`인 수열이 주어진다.
이때 연속된 부분 수열의 합이 `M`이 되는 경우의 수를 구하는 문제이다.

예를 들어 수열이 다음과 같을 때,

```text
1 2 3 4 2 5 3 1 1 2
```

연속된 구간의 합이 `5`가 되는 경우를 찾아야 한다.

---

## 문제 접근

이 문제는 **투 포인터**를 사용해서 풀 수 있다.

연속된 부분 수열의 합을 구해야 하므로 `left`, `right` 두 개의 포인터를 사용한다.

* `right`를 이동시키면 구간의 크기가 커진다.
* `left`를 이동시키면 구간의 크기가 작아진다.
* 현재 구간의 합이 `M`보다 작으면 `right`를 이동한다.
* 현재 구간의 합이 `M`보다 크거나 같으면 `left`를 이동한다.
* 현재 구간의 합이 `M`과 같으면 정답 개수를 증가시킨다.

이 문제의 수열 원소는 모두 자연수이기 때문에, 구간을 늘리면 합이 증가하고 구간을 줄이면 합이 감소한다.
따라서 투 포인터를 사용할 수 있다.

---

## 코드

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
res = 0

while left <= right:
    if res >= m:
        if res == m:
            cnt += 1
        res -= lst[left]
        left += 1
    else:
        if right < n:
            res += lst[right]
            right += 1
        else:
            break

print(cnt)
```

---

## 코드 설명

```python
left = 0
right = 0
cnt = 0
res = 0
```

`left`와 `right`는 현재 구간의 시작과 끝을 나타낸다.
`res`는 현재 구간의 합이고, `cnt`는 합이 `M`이 되는 경우의 수이다.

---

```python
if res >= m:
```

현재 구간의 합이 `M`보다 크거나 같다면 구간을 줄여야 한다.
따라서 `left`를 이동시킨다.

---

```python
if res == m:
    cnt += 1
```

현재 구간의 합이 `M`과 같다면 정답이므로 `cnt`를 1 증가시킨다.

---

```python
res -= lst[left]
left += 1
```

현재 구간에서 왼쪽 값을 제거하고 `left`를 오른쪽으로 한 칸 이동한다.

---

```python
else:
    if right < n:
        res += lst[right]
        right += 1
    else:
        break
```

현재 구간의 합이 `M`보다 작다면 구간을 늘려야 한다.
따라서 `right` 위치의 값을 더하고 `right`를 오른쪽으로 한 칸 이동한다.

만약 `right`가 배열의 끝에 도달했다면 더 이상 구간을 늘릴 수 없으므로 반복문을 종료한다.

---

## 핵심 아이디어

```python
if res >= m:
    왼쪽 포인터 이동
else:
    오른쪽 포인터 이동
```

현재 합이 크거나 같으면 왼쪽을 줄이고,
현재 합이 작으면 오른쪽을 늘리는 방식이다.

---

## 시간 복잡도

각 포인터는 최대 `N`번만 이동한다.

따라서 시간 복잡도는

```text
O(N)
```

이다.

---
