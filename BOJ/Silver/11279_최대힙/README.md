# 📌 BOJ 11279 - 최대 힙

## 🔗 문제 링크
https://www.acmicpc.net/problem/11279


## 📖 문제 설명

최대 힙을 구현하는 문제이다.

- 자연수 `x`가 주어지면 배열에 `x`를 넣는다.
- `0`이 주어지면 배열에서 가장 큰 값을 출력하고 제거한다.
- 배열이 비어 있는데 `0`이 들어오면 `0`을 출력한다.

## 💡 핵심 아이디어

Python의 `heapq`는 **최소 힙(min heap)** 구조이다.  
하지만 이 문제는 **최대 힙(max heap)**을 요구한다.

👉 해결 방법:
- 값을 넣을 때 `-x`로 넣는다.
- 값을 꺼낼 때 다시 `-`를 붙여서 출력한다.

즉, 부호를 반대로 뒤집어서 최대 힙처럼 사용하는 방식이다.


## ⚙️ 알고리즘

1. 입력을 받는다.
2. `0`이 아닌 경우:
   - `heapq.heappush(heap, -x)`로 삽입
3. `0`인 경우:
   - 힙이 비어있지 않으면 `-heapq.heappop(heap)` 출력
   - 비어있으면 `0` 출력


## 💻 코드

```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)
```

## ⏱️ 시간 복잡도
- 삽입: O(log N)
- 삭제: O(log N)
- 전체: O(N log N)

## 🔥 관련 개념
- 힙(Heap)
- 우선순위 큐(Priority Queue)
- 최대 힙 구현 (heapq 활용)

## ✅ 한 줄 정리

**👉 heapq는 최소 힙 → 부호 반전으로 최대 힙처럼 사용**