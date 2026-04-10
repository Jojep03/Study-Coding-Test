# 🥇 BOJ 2512 - 예산

## 📌 문제 설명

각 지방에서 요청한 예산이 주어지고,  
국가 총 예산 `M`이 제한되어 있을 때,

모든 지방에 동일한 **상한액(cap)** 을 적용하여  
다음과 같이 예산을 배정합니다.

배정 예산 = min(요청 예산, cap)


이때, **총합이 M을 넘지 않도록 하는 최대 cap**을 구하는 문제입니다.

---

## 💡 풀이 방법 1: 직접 계산 (그리디 느낌)

### ✅ 아이디어

- 예산을 정렬한 뒤
- 앞에서부터 하나씩 확정하면서
- 남은 예산을 남은 지방 수로 나눠 cap을 계산

---

### ⚙️ 코드

```python
import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())

x.sort()
max_x = 0

if sum(x) > m:
    for i in range(n):
        ans = (m - sum(x[:i])) // len(x[i:])
        max_x = max(max_x, ans)
else:
    max_x = max(x)

print(max_x)
```

---

### ⚠️ 단점
sum(x[:i])를 반복해서 계산 → **비효율적 (O(N²))**


입력이 커지면 시간 초과 가능

---

## 💡 풀이 방법 2: 이분 탐색 (정석 풀이)

### ✅ 아이디어
- cap을 정하고 총합을 계산
- 총합이 M 이하이면 cap을 키움
- 초과하면 cap을 줄임

### 👉 “조건을 만족하는 최대값” → 이분탐색

## ⚙️ 코드
```python
import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())

start = 0
end = max(x)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for budget in x:
        total += min(budget, mid)

    if total <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
```

---

## 🚀 핵심 포인트
- min(요청값, cap)으로 총합 계산


- 총합이 M 이하 → 더 크게 시도


- 총합이 초과 → 줄이기

## 📊 두 풀이 비교
| 구분     | 직접 계산 | 이분 탐색      |
| ------ | ----- | ---------- |
| 시간복잡도  | O(N²) | O(N log N) |
| 안정성    | 낮음    | 높음 (정석)    |
