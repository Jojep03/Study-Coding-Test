# 📌 백준 11286 - 절댓값 힙

## 🔗 문제 링크

* https://www.acmicpc.net/problem/11286

## 🧠 문제 설명

정수 배열에서 다음 연산을 수행하는 프로그램을 작성하는 문제입니다.

* `0`이 입력되면 → 절댓값이 가장 작은 값을 출력하고 제거
* `0`이 아니면 → 해당 값을 배열에 추가

### 📌 우선순위 조건

1. 절댓값이 작은 값이 우선
2. 절댓값이 같으면 실제 값이 작은 값 (음수가 먼저)


## 💡 해결 아이디어

Python의 `heapq`는 **최소 힙**을 제공하므로, 우선순위를 직접 설정해야 합니다.

👉 핵심 전략:

```python
(abs값, 실제값)
```

이 형태로 힙에 넣으면:

* 먼저 `abs값` 기준으로 비교
* 같으면 `실제값` 비교

즉, 문제 조건을 그대로 만족합니다.

## ⚠️ 중요한 포인트

* `heapq`는 **정렬된 리스트가 아님**
* 오직 `heap[0]`만 최솟값을 보장
* 내부 순서는 계속 바뀔 수 있음

예:

```python
[(1, 1), (2, -2), (2, 2)]
```

👉 `(2, -2)` 위치가 바뀌는 건 정상 (힙 구조 특성)


## 🧾 코드

```python
import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    i = int(input())

    if i != 0:
        heapq.heappush(heap, (abs(i), i))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
```

## 🚀 시간 복잡도

* 삽입: `O(log N)`
* 삭제: `O(log N)`
* 전체: `O(N log N)`

## 🎯 핵심 요약

* 절댓값 기준 정렬 → `(abs(i), i)` 사용
* 힙은 완전 정렬 ❌, 루트만 보장 ⭕
* 조건이 있는 우선순위 문제 → 튜플 활용이 핵심

