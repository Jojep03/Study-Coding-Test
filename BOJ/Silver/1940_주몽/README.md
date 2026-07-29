# 백준 1940 - 주몽

## 문제 핵심

갑옷 하나를 만들기 위해서는 서로 다른 두 재료의 번호를 더했을 때 `M`이 되어야 한다.

즉, 재료 번호가 들어 있는 배열에서

```python
lst[left] + lst[right] == m
```

을 만족하는 두 재료의 쌍이 몇 개인지 구하는 문제이다.

---

## 풀이 방법

배열을 오름차순으로 정렬한 뒤 **투 포인터**를 사용한다.

```python
lst.sort()

left = 0
right = n - 1
```

`left`는 가장 작은 값을 가리키고, `right`는 가장 큰 값을 가리킨다.

두 재료의 합을 계산한다.

```python
temp = lst[left] + lst[right]
```

---

## 포인터 이동

### 합이 `M`보다 작은 경우

```python
if temp < m:
    left += 1
```

현재 합이 목표값보다 작으므로 합을 더 크게 만들어야 한다.

따라서 작은 값을 가리키는 `left`를 오른쪽으로 이동한다.

---

### 합이 `M`보다 큰 경우

```python
elif temp > m:
    right -= 1
```

현재 합이 목표값보다 크므로 합을 더 작게 만들어야 한다.

따라서 큰 값을 가리키는 `right`를 왼쪽으로 이동한다.

---

### 합이 `M`과 같은 경우

```python
else:
    cnt += 1
    left += 1
    right -= 1
```

갑옷을 만들 수 있는 재료의 조합을 찾았으므로 `cnt`를 증가시킨다.

재료 번호는 모두 고유하고, 사용한 두 재료는 다시 사용할 수 없으므로 양쪽 포인터를 모두 이동한다.

---

## 전체 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))

lst.sort()

cnt = 0
left = 0
right = n - 1

while left < right:
    temp = lst[left] + lst[right]

    if temp < m:
        left += 1
    elif temp > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)
```

---

## 시간 복잡도

배열 정렬에

```text
O(N log N)
```

투 포인터 탐색에

```text
O(N)
```

이 걸린다.

따라서 전체 시간 복잡도는

```text
O(N log N)
```

이다.

---

## 핵심 정리

```text
합이 작다 → left 증가
합이 크다 → right 감소
합이 같다 → 정답 증가 후 양쪽 포인터 이동
```

정렬된 배열에서 두 수의 합을 찾는 대표적인 투 포인터 문제이다.
