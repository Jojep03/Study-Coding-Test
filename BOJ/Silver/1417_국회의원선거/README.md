# 백준 1417번 - 국회의원 선거

## 🔗 문제 링크
https://www.acmicpc.net/problem/1417

## 📌 문제 설명
다솜이가 국회의원 선거에서 당선되기 위해  
다른 후보의 표를 매수하여 자신의 표를 증가시킬 수 있다.

- 한 번 매수하면:
  - 다른 후보 표 -1
  - 다솜 표 +1

다솜이가 **다른 모든 후보보다 표가 많아질 때까지**  
최소 몇 번 매수해야 하는지 구하는 문제.

## 💡 핵심 아이디어

### 우선순위:
항상 **현재 가장 표가 많은 후보**의 표를 빼앗는 것이 최적이다.

즉,

1. 다른 후보 중 최댓값 찾기
2. 그 후보 표 1 감소
3. 다솜 표 1 증가
4. 반복

## 🚀 사용 알고리즘
### 최대 힙 (Priority Queue)

Python의 `heapq`는 최소 힙이므로  
음수로 저장해서 최대 힙처럼 사용한다.

```python
heapq.heappush(heap, -x)
```

## ⚠️ 주의할 점
1. ``n = 1`` **예외 처리**

    다솜이 혼자 후보면 바로 0 출력

2. **공동 1등도 안 됨**

    다솜이는 **무조건 단독 1등**이어야 하므로

```python
while -heap[0] >= target:
```

``>``가 아니라 ``>=`` 사용

예:

- 다솜 5
- 상대 5

→ 공동 1등이므로 한 표 더 필요

## ✅ 코드
```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())
target = int(input())

heap = []
for _ in range(n - 1):
    x = int(input())
    heapq.heappush(heap, -x)

res = 0

while heap and -heap[0] >= target:
    vote = -heapq.heappop(heap)
    vote -= 1
    target += 1
    res += 1
    heapq.heappush(heap, -vote)

print(res)
```

## ⏱️ 시간 복잡도
#### 한 번 매수할 때:
- pop: ``O(log N)``
- push: ``O(log N)``

#### 총:

최대 매수 횟수를 K라 하면

**O(K log N)**

입력 범위가 작아서 충분히 가능.

## 🎯 핵심 한 줄

**가장 표가 많은 상대 후보를 계속 1씩 낮추면 최소 횟수로 다솜이를 1등으로 만들 수 있다.** 