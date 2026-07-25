# 백준 1253 - 좋다

## 문제 핵심

수열에 있는 어떤 수가 다른 두 수의 합으로 표현될 수 있다면 그 수를 **좋다(GOOD)**라고 한다.

즉, 각 숫자 `lst[i]`에 대해

```python
lst[left] + lst[right] == lst[i]
```

를 만족하는 서로 다른 두 인덱스가 존재하는지 확인하면 된다.

주의할 점은 같은 값을 사용할 수는 있지만, 같은 인덱스를 두 번 사용할 수는 없다는 것이다.

---

## 풀이 방법

각 숫자를 목표값으로 정한 뒤, 정렬된 배열에서 투 포인터를 사용한다.

```python
for i in range(n):
```

`lst[i]`를 두 수의 합으로 만들 수 있는지 확인한다.

투 포인터는 배열의 양 끝에서 시작한다.

```python
left = 0
right = n - 1
```

현재 두 수의 합을 구한다.

```python
temp = lst[left] + lst[right]
```

---

## 포인터 이동

현재 합이 목표값보다 작다면 더 큰 값이 필요하므로 왼쪽 포인터를 증가시킨다.

```python
if temp < lst[i]:
    left += 1
```

현재 합이 목표값보다 크다면 더 작은 값이 필요하므로 오른쪽 포인터를 감소시킨다.

```python
elif temp > lst[i]:
    right -= 1
```

두 수의 합이 목표값과 같다면 좋은 수이므로 개수를 증가시키고 반복문을 종료한다.

```python
else:
    cnt += 1
    break
```

하나의 목표값은 좋은 수인지 아닌지만 판단하면 되기 때문에, 한 번 찾으면 더 탐색할 필요가 없다.

---

## 자기 자신 제외

두 수를 선택할 때 목표값 자신의 인덱스는 사용할 수 없다.

따라서 `left`나 `right`가 `i`와 같다면 해당 포인터를 이동시킨다.

```python
if left == i:
    left += 1
    continue

if right == i:
    right -= 1
    continue
```

값이 같더라도 인덱스가 다르면 사용할 수 있다.

예를 들어 다음 수열에서는

```text
0 0 0
```

각각의 `0`을 나머지 두 개의 `0`으로 만들 수 있으므로 세 수 모두 좋은 수이다.

---

## 전체 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0

for i in range(n):
    left = 0
    right = n - 1

    while left < right:
        if left == i:
            left += 1
            continue

        if right == i:
            right -= 1
            continue

        temp = lst[left] + lst[right]

        if temp < lst[i]:
            left += 1
        elif temp > lst[i]:
            right -= 1
        else:
            cnt += 1
            break

print(cnt)
```

---

## 시간 복잡도

배열 정렬에

```text
O(N log N)
```

각 숫자마다 투 포인터 탐색에 `O(N)`이 필요하고, 이를 `N`번 반복하므로

```text
O(N²)
```

전체 시간 복잡도는

```text
O(N²)
```

이다.

---

## 핵심 정리

* 배열을 오름차순으로 정렬한다.
* 각 숫자를 목표값으로 설정한다.
* 양 끝에서 투 포인터 탐색을 시작한다.
* 합이 작으면 `left`를 증가시킨다.
* 합이 크면 `right`를 감소시킨다.
* 목표값 자신의 인덱스는 사용하지 않는다.
* 합이 목표값과 같으면 좋은 수이므로 개수를 증가시키고 종료한다.
