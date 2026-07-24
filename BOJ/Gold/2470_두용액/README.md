# 백준 2470 - 두 용액

## 문제 핵심

용액들이 주어지고, 서로 다른 두 용액을 섞었을 때

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

`2470번`은 입력으로 주어지는 배열이 정렬되어 있다는 보장이 없기 때문에 먼저 **오름차순 정렬**을 해준다.

```python
lst.sort()
```

정렬한 뒤에는 **투 포인터**를 사용한다.

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
if abs(res) > abs(temp):
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

배열이 오름차순으로 정렬되어 있으므로 `left`를 오른쪽으로 이동시킨다.

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

이런 식으로 두 포인터를 이동하면 된다.

---

## 예시

예를 들어

```text
[-99, -2, -1, 4, 98]
```

이 있다고 하면 처음에는

```text
left = -99
right = 98
```

이므로

```text
합 = -1
```

이다.

현재 합이 음수이므로 합을 더 크게 만들기 위해 `left`를 오른쪽으로 이동한다.

```text
[-99, -2, -1, 4, 98]
       ↑          ↑
     left       right
```

반대로 합이 양수라면 `right`를 왼쪽으로 이동한다.

이런 식으로 두 포인터를 가운데 방향으로 이동시키면서 `0`에 가장 가까운 합을 찾는다.

---

## 주의할 점

### 입력 배열을 먼저 정렬해야 한다

`2467번 용액`과 풀이 방식은 거의 동일하지만 중요한 차이가 있다.

`2467번`은 입력 자체가 이미 오름차순으로 주어지지만, `2470번`은 정렬되어 있다는 보장이 없다.

따라서 반드시

```python
lst.sort()
```

를 먼저 해줘야 한다.

투 포인터에서

```python
temp < 0 → left 이동
temp > 0 → right 이동
```

이라는 판단이 가능한 이유도 배열이 정렬되어 있기 때문이다.

---

### `res`도 같이 갱신해야 한다

정답이 되는 인덱스만 저장하면 안 되고 현재까지 가장 `0`에 가까운 합인 `res`도 같이 갱신해야 한다.

```python
if abs(res) > abs(temp):
    res = temp
    res_left = left
    res_right = right
```

만약

```python
res = temp
```

를 하지 않으면 계속 처음 값과 비교하게 되므로 이후 더 좋지 않은 값이 다시 정답으로 저장될 수 있다.

따라서 정답 인덱스와 함께 `res`도 반드시 갱신해야 한다.

---

### 합이 0이면 바로 종료 가능

두 용액의 합이

```python
temp == 0
```

이라면 `0`보다 더 가까운 값은 존재할 수 없다.

따라서 바로 반복문을 종료할 수 있다.

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
lst.sort()

left = 0
right = n - 1

res_left = left
res_right = right
res = lst[res_left] + lst[res_right]

while left < right:
    temp = lst[left] + lst[right]

    if abs(res) > abs(temp):
        res = temp
        res_left = left
        res_right = right

    if temp == 0:
        break
    elif temp < 0:
        left += 1
    else:
        right -= 1

print(lst[res_left], lst[res_right])
```

## 핵심 정리

* 두 용액의 합이 `0`에 가장 가까운 조합 찾기 → 투 포인터
* `2470번`은 입력이 정렬되어 있지 않을 수 있으므로 먼저 `lst.sort()`
* 처음에는 `left = 0`, `right = n - 1`
* 합이 음수이면 더 크게 만들어야 하므로 `left += 1`
* 합이 양수이면 더 작게 만들어야 하므로 `right -= 1`
* `abs(temp)`가 더 작으면 정답 갱신
* 정답 갱신 시 `res`도 반드시 같이 갱신
* 합이 `0`이면 가장 최적이므로 바로 종료 가능

### 시간 복잡도

정렬에

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
