# [BOJ 2563] 색종이 - Python

## 문제 설명

가로, 세로 크기가 각각 100인 도화지 위에 색종이를 붙인다.

색종이는 항상 가로 10, 세로 10 크기이며, 여러 장의 색종이가 겹칠 수 있다.

색종이가 붙은 전체 영역의 넓이를 구하는 문제이다.

## 풀이 아이디어

도화지를 `100 x 100` 크기의 2차원 배열로 생각한다.

처음에는 아무 색종이도 붙지 않았으므로 모든 칸을 `0`으로 둔다.

색종이의 왼쪽 아래 좌표가 `(x, y)`로 주어지면, 해당 색종이는 다음 범위를 차지한다.

```python
x ~ x + 9
y ~ y + 9
```

즉, 총 `10 x 10 = 100`개의 칸을 덮는다.

그래서 각 색종이마다 해당 영역을 `1`로 바꿔준다.

겹치는 부분은 이미 `1`이어도 다시 `1`로 바뀌기 때문에 중복 계산되지 않는다.

마지막에는 도화지 전체를 돌면서 값이 `1`인 칸의 개수를 세면 된다.

## 코드

```python
import sys

input = sys.stdin.readline

n = int(input())

papers = []
for _ in range(n):
    x, y = map(int, input().split())
    papers.append((x, y))

board = [[0] * 100 for _ in range(100)]

for x, y in papers:
    target_x = x + 10
    target_y = y + 10
    for i in range(x, target_x):
        for j in range(y, target_y):
            board[i][j] = 1
res = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            res += 1
print(res)
print(sum(map(sum, board)))
```

## 코드 설명

```python
board = [[0] * 100 for _ in range(100)]
```

100 x 100 크기의 도화지를 만든다.

`0`은 아직 색종이가 붙지 않은 칸을 의미한다.

```python
for _ in range(n):
    x, y = map(int, input().split())
```

색종이의 개수만큼 좌표를 입력받는다.

```python
for i in range(x, x + 10):
    for j in range(y, y + 10):
        board[i][j] = 1
```

색종이가 덮는 10 x 10 영역을 전부 `1`로 바꾼다.

이미 `1`인 칸을 다시 `1`로 바꿔도 상관없기 때문에 겹치는 영역도 자연스럽게 처리된다.

```python
if board[i][j] == 1:
    res += 1
```

도화지 전체를 확인하면서 색종이가 붙은 칸의 개수를 센다.

## 정리

이 문제는 실제 넓이를 수식으로 계산하려고 하면 겹치는 부분 때문에 복잡해질 수 있다.

하지만 도화지 크기가 100 x 100으로 작기 때문에, 2차원 배열을 만들어 직접 색칠하는 방식으로 쉽게 해결할 수 있다.

핵심은 다음과 같다.

```python
겹치는 부분도 그냥 1로 칠하면 된다.
```

따라서 마지막에 `1`인 칸의 개수만 세면 색종이가 붙은 전체 넓이가 된다.
