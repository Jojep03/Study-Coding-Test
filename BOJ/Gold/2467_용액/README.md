# 백준 2467 - 용액

## 문제 핵심

오름차순으로 정렬된 용액들이 주어지고, 서로 다른 두 용액을 섞었을 때

```python
두 용액의 합이 0에 가장 가까운 경우
```

를 찾는 문제이다.

즉,

```python
abs(lst[left] + lst[right])
```

가 최소가 되는 두 용액을 찾으면 된다.

---

## 풀이 방법

배열이 이미 **오름차순으로 정렬**되어 있으므로 **투 포인터**를 사용한다.

처음에는 양 끝에 포인터를 둔다.

```python
left = 0
right = n - 1
```

그리고 두 용액의 합을 구한다.

```python
temp = lst[left] + lst[right]
```

현재 합의 절댓값이 지금까지 찾은 값보다 더 작다면 정답을 갱신한다.

```python
if abs(temp) < abs(res):
    res = temp
    res_left = left
    res_right = right
```

---

## 포인터 이동

현재 두 용액의 합이 음수라면

```python
temp < 0
```

합을 `0`에 가깝게 만들기 위해서는 값을 더 크게 만들어야 한다.

배열이 오름차순이므로 `left`를 오른쪽으로 이동시킨다.

```python
left += 1
```

반대로 합이 양수라면

```python
temp > 0
```

합을 더 작게 만들어야 하므로 `right`를 왼쪽으로 이동시킨다.

```python
right -= 1
```

즉,

```python
if temp < 0:
    left += 1
else:
    right -= 1
```

이렇게 이동하면 된다.

---

## 예시

예를 들어

```text
[-99, -2, -1, 4, 98]
```

이라고 하면 처음에는

```text
left = -99
right = 98
```

이므로

```text
합 = -1
```

이다.

합이 음수이므로 더 큰 값을 만들기 위해 `left`를 오른쪽으로 이동한다.

```text
[-99, -2, -1, 4, 98]
       ↑          ↑
     left       right
```

이런 식으로 두 포인터를 가운데 방향으로 이동시키면서 `0`에 가장 가까운 합을 찾는다.

---

## 주의할 점

### `res`도 같이 갱신해야 한다

정답이 되는 인덱스만 갱신하면 안 되고, 현재 가장 좋은 합인 `res`도 같이 갱신해야 한다.

```python
if abs(temp) < abs(res):
    res = temp
    res_left = left
    res_right = right
```

만약

```python
res = temp
```

를 하지 않으면 계속 처음 구한 `res`와 비교하게 된다.

예를 들어 처음 합이 `10`이고 이후에 `3`을 찾았더라도 `res`를 갱신하지 않으면, 그다음 `7`도

```text
7 < 10
```

이므로 정답으로 다시 갱신될 수 있다.

따라서 반드시 `res`를 같이 갱신해야 한다.

---

### 합이 0이면 바로 종료 가능

두 용액의 합이

```python
temp == 0
```

이라면 `0`보다 더 가까운 값은 존재할 수 없다.

따라서 바로 반복문을 종료해도 된다.

```python
if temp == 0:
    break
```

---

## 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

left = 0
right = n - 1

res_left = left
res_right = right
res = lst[res_left] + lst[res_right]

while left < right:
    temp = lst[left] + lst[right]

    if abs(temp) < abs(res):
        res = temp
        res_left = left
        res_right = right

        if temp == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1

print(lst[res_left], lst[res_right])
```

## 핵심 정리

* **정렬된 배열에서 두 수의 합을 확인** → 투 포인터
* 처음에는 `left = 0`, `right = n - 1`
* 합이 음수이면 더 크게 만들어야 하므로 `left += 1`
* 합이 양수이면 더 작게 만들어야 하므로 `right -= 1`
* `abs(temp)`가 더 작으면 정답 갱신
* 정답 갱신 시 `res`도 반드시 같이 갱신
* 합이 `0`이면 가장 최적이므로 바로 종료 가능

### 시간 복잡도

두 포인터가 배열의 양 끝에서 시작하여 한 방향으로만 이동한다.

```text
O(N)
```
