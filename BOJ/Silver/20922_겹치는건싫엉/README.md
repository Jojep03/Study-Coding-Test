# 🥈 BOJ 20922 - 겹치는 건 싫어

## 📌 문제 설명

길이가 `N`인 수열이 주어졌을 때,  
같은 정수가 `K`개 이하로만 들어있는 **최장 연속 부분 수열의 길이**를 구하는 문제입니다.

즉, 부분 수열 안에서 어떤 숫자도 `K`번을 초과해서 등장하면 안 됩니다.

---

## 💡 핵심 아이디어

이 문제는 **투 포인터**를 사용해서 풀 수 있습니다.

`left`, `right` 두 개의 포인터를 사용해서 현재 보고 있는 구간을 관리합니다.

현재 구간은 다음과 같습니다.

```txt
[left, right)
```

즉, `left`는 포함하고 `right`는 아직 포함하지 않은 위치입니다.

---

## 🔄 풀이 과정

1. `right` 위치의 숫자를 현재 구간에 넣을 수 있는지 확인합니다.
2. 해당 숫자의 개수가 `K`보다 작으면 구간에 추가합니다.
3. 이미 `K`개라면 더 넣을 수 없으므로 `left`를 이동시켜 구간을 줄입니다.
4. 매번 현재 구간의 길이 `right - left`를 확인하여 최댓값을 갱신합니다.

---

## 🧠 코드 설명

```python
if cnt[lst[right]] < k:
```

현재 `right` 위치의 숫자가 아직 `K`개보다 적게 사용되었다면 추가할 수 있습니다.

```python
cnt[lst[right]] += 1
right += 1
```

숫자를 현재 구간에 추가하고 `right`를 한 칸 이동합니다.

```python
else:
    cnt[lst[left]] -= 1
    left += 1
```

이미 해당 숫자가 `K`개라면 더 추가할 수 없으므로  
왼쪽 숫자를 제거하고 `left`를 한 칸 이동합니다.

```python
res = max(res, right - left)
```

현재 구간의 길이와 기존 최댓값을 비교해서 갱신합니다.

---

## ✅ 정답 코드

```python
import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
cnt = {i: 0 for i in range(1, n + 1)}
res = 0

while right < n:
    if cnt[lst[right]] < k:
        cnt[lst[right]] += 1
        right += 1
    else:
        cnt[lst[left]] -= 1
        left += 1

    res = max(res, right - left)

print(res)
```

---

## ⏱️ 시간복잡도

```txt
O(N)
```

`left`와 `right`가 각각 최대 `N`번만 이동하기 때문입니다.

---

## 📦 사용 알고리즘

```txt
투 포인터
슬라이딩 윈도우
딕셔너리 / 카운팅
```

---

## 📝 핵심 정리

```txt
같은 숫자가 K개 이하로만 들어가는 가장 긴 연속 부분 수열을 구해야 한다.
현재 구간 안의 숫자 개수를 저장하면서 left, right 포인터를 이동한다.
right 값을 넣을 수 있으면 추가하고, 넣을 수 없으면 left를 줄인다.
```