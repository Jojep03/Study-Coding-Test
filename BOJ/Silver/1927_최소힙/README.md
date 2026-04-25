# 🧩 백준 1927번 - 최소 힙

## 🔗 문제 링크
https://www.acmicpc.net/problem/1927


## 📌 문제 설명

정수 `x`를 입력받는 연산을 수행한다.

- `x ≠ 0` → 배열에 추가
- `x = 0` → 배열에서 가장 작은 값을 출력하고 제거  
  - 배열이 비어있으면 `0` 출력

## 💡 핵심 아이디어

이 문제는 **최소값을 빠르게 꺼내는 자료구조**가 핵심이다.

👉 Python의 `heapq`를 사용하면 해결 가능

- `heapq`는 기본적으로 **최소 힙 (Min Heap)** 구조
- 가장 작은 값이 항상 루트에 위치
- 삽입 / 삭제 모두 `O(log N)`

## ⚙️ 알고리즘

1. 빈 리스트 `heap` 생성
2. 입력값을 하나씩 처리
   - 값이 0이면
     - heap이 비어있지 않으면 → `heappop`
     - 비어있으면 → `0 출력`
   - 값이 0이 아니면 → `heappush`

## 🧪 코드

```python
import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    i = int(input())

    if i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)
```

## ⏱️ 시간 복잡도
- 삽입: ``O(log N)``
- 삭제: ``O(log N)``
- 전체: ``O(N log N)``

## 📝 정리
- 최소값을 빠르게 찾는 문제 → **힙 사용**
- Python에서는 ``heapq``로 바로 해결 가능
- 조건 분기만 잘 처리하면 되는 **기본 힙 문제**