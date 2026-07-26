# 백준 2230 - 수 고르기

## 문제 핵심

`N`개의 수 중에서 서로 다른 두 수를 골랐을 때, 두 수의 차이가 `M` 이상인 경우 중 가장 작은 차이를 구하는 문제이다.

즉,

```python
lst[right] - lst[left] >= m
```

을 만족하는 값 중 최솟값을 찾으면 된다.

---

## 풀이 방법

두 수의 차이를 비교해야 하므로 먼저 배열을 오름차순으로 정렬한다.

```python
lst.sort()
```

정렬된 배열에서 두 개의 포인터를 배열의 왼쪽에 둔다.

```python
left = 0
right = 0
```

정렬되어 있기 때문에 항상

```python
lst[right] >= lst[left]
```

이므로 두 수의 차이는 다음과 같이 구할 수 있다.

```python
temp = lst[right] - lst[left]
```

따라서 `abs()`는 사용하지 않아도 된다.

---

## 포인터 이동

### 차이가 `M`보다 작은 경우

```python
if temp < m:
    right += 1
```

현재 차이가 너무 작으므로 더 큰 수를 선택해야 한다.

따라서 `right`를 오른쪽으로 이동시켜 두 수의 차이를 증가시킨다.

---

### 차이가 `M` 이상인 경우

```python
else:
    res = min(res, temp)
    left += 1
```

현재 차이는 문제의 조건을 만족하므로 정답 후보가 된다.

그다음 더 작은 차이를 찾기 위해 `left`를 오른쪽으로 이동시켜 두 수의 차이를 감소시킨다.

---

## 정답 초기값

```python
res = float("inf")
```

`float("inf")`는 양의 무한대를 의미한다.

처음에는 아직 정답 후보를 찾지 못했기 때문에 매우 큰 값으로 초기화한다.

그러면 처음 조건을 만족하는 차이가 발견되었을 때 무조건 `res`에 저장된다.

```python
res = min(res, temp)
```

---

## 코드

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

left = 0
right = 0
res = float("inf")

while right < n:
    temp = lst[right] - lst[left]

    if temp < m:
        right += 1
    else:
        res = min(res, temp)

        if temp == m:
            break

        left += 1

print(res)
```

---

## `temp == m`이면 종료 가능한 이유

문제에서 두 수의 차이는 반드시 `M` 이상이어야 한다.

따라서 차이가 정확히 `M`인 경우를 찾았다면 가능한 정답 중 가장 작은 값을 찾은 것이다.

```python
if temp == m:
    break
```

더 이상 탐색할 필요 없이 반복문을 종료할 수 있다.

---

## 시간 복잡도

배열 정렬:

```text
O(N log N)
```

투 포인터 탐색:

```text
O(N)
```

따라서 전체 시간 복잡도는

```text
O(N log N)
```

이다.

---

## 핵심 정리

* 배열을 오름차순으로 정렬한다.
* 차이가 `M`보다 작으면 `right`를 증가시킨다.
* 차이가 `M` 이상이면 정답을 갱신하고 `left`를 증가시킨다.
* 정렬된 배열이므로 `abs()`는 필요하지 않다.
* 차이가 정확히 `M`이면 바로 종료할 수 있다.
