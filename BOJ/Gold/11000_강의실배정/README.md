# 🥇 BOJ 11000 - 강의실 배정

## 📌 문제 설명
각 강의의 시작 시간 `S`, 종료 시간 `T`가 주어질 때  
모든 강의를 진행하기 위해 필요한 **최소 강의실 개수**를 구하는 문제입니다.

### 핵심 조건
- 한 강의가 끝나는 시간과 다른 강의 시작 시간이 같으면 같은 강의실 사용 가능

---

## 💡 풀이 아이디어

### 핵심 생각
현재 사용 중인 강의실 중 **가장 빨리 끝나는 시간**만 알면 됩니다.

따라서:

```txt
heap = 현재 사용 중인 강의실들의 종료 시간
heap[0] = 가장 빨리 끝나는 강의실
```

## 💡 풀이 아이디어
강의를 시작 시간 기준으로 정렬한 뒤,
현재 사용 중인 강의실들의 **종료 시간**을 최소 힙에 저장합니다.

힙의 가장 작은 값 ``heap[0]``은
현재 강의실 중에서 **가장 빨리 끝나는 강의의 종료 시간**입니다.

새로운 강의의 시작 시간이 ``heap[0]``보다 크거나 같다면
가장 빨리 끝난 강의실을 재사용할 수 있습니다.

반대로 새로운 강의의 시작 시간이 ``heap[0]``보다 작다면
아직 비어 있는 강의실이 없으므로 새로운 강의실이 필요합니다.


## ⚙️ 사용 알고리즘
   
- 정렬 
- 최소 힙 (Priority Queue)


## ✅ 버전 1 - 첫 강의를 먼저 넣는 방식
```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))

lst.sort()

heap = []
heapq.heappush(heap, lst[0][1])

for i in range(1, n):
    s, t = lst[i]

    if s < heap[0]:
        heapq.heappush(heap, t)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, t)

print(len(heap))
```

### 특징
- 첫 번째 강의를 미리 힙에 넣고 시작
- 두 번째 강의부터 비교

## ✅ 버전 2

```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))

lst.sort()

heap = []

for s, t in lst:
    if heap and heap[0] <= s:
        heapq.heappop(heap)

    heapq.heappush(heap, t)

print(len(heap))
```

### 특징
- 빈 힙에서 시작
- 모든 강의를 동일한 방식으로 처리
- heap and 로 빈 힙 예외 처리

## 🔥 두 버전 차이

### 버전 1
```python
heapq.heappush(heap, lst[0][1])
for i in range(1, n):
```
### 버전 2
```python
for s, t in lst:
```

## ⚠️ 주의할 점
### ❌ 틀린 방식
```python
heapq.heappush(heap, (s, t))
```

시작 시간 기준으로 정렬될 수 있어서 잘못됨.

### ✅ 올바른 방식
```python
heapq.heappush(heap, t)
```

종료 시간만 넣어야 가장 빨리 끝나는 강의를 바로 확인 가능.

## ⏱️ 시간 복잡도
- 정렬: ``O(N log N)``
- 힙 연산: ``O(N log N)``
- 총합: ``O(N log N)``
