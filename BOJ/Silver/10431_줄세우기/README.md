# 📘 BOJ 10431 - 줄세우기

## 🧾 문제 설명

학생들이 한 줄로 서 있습니다.  
앞에서부터 한 명씩 들어오며, 자기보다 키가 큰 학생 앞에 서게 됩니다.

이 과정에서 발생하는 이동 횟수를 구하는 문제입니다.

---

## 💡 핵심 아이디어

이 문제는 삽입 정렬 과정에서 발생하는 swap 횟수를 구하는 문제입니다.

---

## 🧠 풀이 방법 1 - 버블 정렬 방식

### ✔ 개념
모든 쌍을 비교하면서 swap 횟수를 카운트

### 💻 코드

```python
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    cnt = 0
    
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1
    
    print(arr[0], cnt)
```

### ⚠ 특징
- 구현은 쉽지만 비효율적
- 문제 의도와 완전히 일치하지는 않음

---

## 🧠 풀이 방법 2 - 삽입 정렬 방식

### ✔ 개념
학생이 한 명씩 들어오면서 자기 위치를 찾는 과정

### 💻 코드

```python
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    cnt = 0
    
    for i in range(2, len(arr)):
        j = i
        while j > 1 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            cnt += 1
            j -= 1
    
    print(arr[0], cnt)
```

### 🔥 핵심 포인트
- 새로운 학생이 들어올 때마다 왼쪽으로 이동
- swap 횟수 = 이동 횟수

---

## ⚡ 시간 복잡도

- O(N²)
- N ≤ 20이라 충분히 빠름


---

## ✅ 한 줄 정리

삽입 정렬을 이용해 학생을 줄에 끼워 넣는 과정에서 발생하는 이동 횟수를 구하는 문제이다.