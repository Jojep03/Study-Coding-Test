# 백준 7662번 - 이중 우선순위 큐

## 문제 링크

https://www.acmicpc.net/problem/7662

---

## 문제 설명

정수 삽입과 최댓값/최솟값 삭제를 수행하는 **이중 우선순위 큐** 문제입니다.

| 명령어 | 의미 |
|---|---|
| `I n` | 정수 `n` 삽입 |
| `D 1` | 최댓값 삭제 |
| `D -1` | 최솟값 삭제 |

---

## 사용 알고리즘

- 최소 힙
- 최대 힙
- Lazy Deletion
- `heapq`

---

## 핵심 아이디어

Python의 `heapq`는 최소 힙만 지원하므로 힙을 두 개 사용합니다.

```python
q_min = []  # 최솟값 관리
q_max = []  # 최댓값 관리
```

최대 힙은 값을 음수로 바꿔 저장합니다.

```python
heapq.heappush(q_max, (-n, i))
heapq.heappush(q_min, (n, i))
```

여기서 i는 중복값을 구분하기 위한 고유 번호입니다.

## Lazy Deletion

한쪽 힙에서 삭제한 값은 다른 힙에 그대로 남아있을 수 있습니다.

그래서 visited 배열로 해당 값이 살아있는지 관리합니다.

```python
visited[i] = True   # 삽입됨
visited[i] = False  # 삭제됨
```

힙의 맨 위 값이 이미 삭제된 값이면 제거합니다.

```python
while heap and not visited[heap[0][1]]:
    heapq.heappop(heap)
```

## 최댓값 삭제
```python
while q_max and not visited[q_max[0][1]]:
    heapq.heappop(q_max)
```
최대 힙의 맨 위가 이미 삭제된 값이면 제거합니다.

```python
if q_max:
    visited[q_max[0][1]] = False
    heapq.heappop(q_max)
```

유효한 값이 있으면 ``visited``를 ``False``로 바꾸고 삭제합니다.

최솟값도 똑같은 과정을 수행합니다.

## 최종 유령값 제거
```python
while q_max and not visited[q_max[0][1]]:
    heapq.heappop(q_max)

while q_min and not visited[q_min[0][1]]:
    heapq.heappop(q_min)
```

모든 연산이 끝난 뒤에도
각 힙의 맨 위에 유령값이 남아있을 수 있습니다.

따라서 출력 전에 한 번 더 정리합니다.


## 예시 흐름
### 입력
```txt
I 5
I 3
D -1
```

### 삽입 후 상태
```txt
q_min = [(3, 1), (5, 0)]
q_max = [(-5, 0), (-3, 1)]
visited = [True, True]
```
### ``D -1`` 실행

최솟값 ``3`` 삭제

```python
visited[1] = False
```

최소 힙에서는 ``3``이 제거되지만,
최대 힙에는 ``3``이 아직 남아있습니다.

```txt
q_min = [(5, 0)]
q_max = [(-5, 0), (-3, 1)]
visited = [True, False]
```

이때 ``(-3, 1)``은 이미 삭제된 유령값입니다.

나중에 최대 힙의 맨 위로 올라오면 제거됩니다.

## 핵심 포인트
- 최소 힙과 최대 힙을 둘 다 사용한다.
- 최대 힙은 음수로 저장한다.
- 중복값 구분을 위해 (값, 인덱스) 형태로 저장한다.
- visited 배열로 삭제 여부를 관리한다.
- 이미 삭제된 유령값은 힙의 top에 올라왔을 때 제거한다.
- 출력 전에도 유령값을 한 번 더 제거한다.

## ⏱️ 시간 복잡도

힙에서 값을 꺼내거나 넣는 연산은 각각 `O(log K)`입니다.

전체 연산 개수가 K개이므로 시간 복잡도는 다음과 같습니다.
~~~txt
O(K log K)
~~~

## 한 줄 정리

**두 개의 힙과 visited 배열을 이용해 최댓값/최솟값 삭제를 처리하는 문제**