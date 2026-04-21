# 백준 10866번 - 덱

## 문제 링크
https://www.acmicpc.net/problem/10866

## 문제 설명
정수를 저장하는 덱(Deque)을 구현하는 문제입니다.

주어지는 명령에 따라 다음과 같은 연산을 수행해야 합니다.

- `push_front X` : 정수 `X`를 덱의 앞에 넣기
- `push_back X` : 정수 `X`를 덱의 뒤에 넣기
- `pop_front` : 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력. 없으면 `-1`
- `pop_back` : 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력. 없으면 `-1`
- `size` : 덱에 들어있는 정수의 개수 출력
- `empty` : 덱이 비어있으면 `1`, 아니면 `0`
- `front` : 덱의 가장 앞에 있는 정수 출력. 없으면 `-1`
- `back` : 덱의 가장 뒤에 있는 정수 출력. 없으면 `-1`

---

## 핵심 아이디어
파이썬의 `collections.deque`를 사용하면 덱의 앞과 뒤에서 값을 넣고 빼는 연산을 빠르게 처리할 수 있습니다.

이 문제에서 중요한 점은 다음 두 가지입니다.

### 1. `empty`는 따로 변수로 관리할 필요가 없음
처음 코드에서는 `empty` 변수를 만들어서 관리하려고 했지만,  
실제로는 **현재 덱이 비어있는지만 확인하면 바로 답을 출력할 수 있습니다.**

```python
print(1 if not lst else 0)
```

## 2. pop_front, pop_back는 값을 꺼낸 뒤 출력해야 함

이 문제는 단순히 값을 제거하는 것이 아니라,
**제거한 값을 출력해야 합니다.**

예를 들어:
```python
print(lst.popleft() if lst else -1)
```
처럼 작성해야 합니다.

## 풀이 코드

```python
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
lst = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        lst.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        lst.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(lst.popleft() if lst else -1)
    elif cmd[0] == 'pop_back':
        print(lst.pop() if lst else -1)
    elif cmd[0] == 'size':
        print(len(lst))
    elif cmd[0] == 'empty':
        print(1 if not lst else 0)
    elif cmd[0] == 'front':
        print(lst[0] if lst else -1)
    elif cmd[0] == 'back':
        print(lst[-1] if lst else -1)
```
## ⏱️ 시간 복잡도

각 명령은 ``deque``를 사용하면 대부분 ``O(1)``에 처리할 수 있습니다.

명령이 총 ``N``개 들어오므로 전체 시간 복잡도는

**O(N)**

입니다.

## 🧠 정리

이 문제는 덱 자료구조의 기본 연산을 구현하는 문제입니다.

핵심은:

- ``empty``를 따로 변수로 관리하지 말고 덱이 비었는지 바로 확인하기
- ``pop_front``, ``pop_back``는 값을 제거만 하지 말고 **출력까지 해야 한다는 점**

이 두 부분만 조심하면 쉽게 해결할 수 있습니다.