# [BOJ] 12847번 - 꿀 아르바이트

## 문제 설명

준수는 방학 동안 `m`일 동안 아르바이트를 할 수 있다.
`n`일 동안 받을 수 있는 급여가 주어졌을 때, 연속된 `m`일 동안 일해서 받을 수 있는 최대 급여를 구하는 문제이다.

## 문제 풀이

이 문제는 연속된 `m`개의 합 중 최댓값을 구하면 된다.

처음 `m`일의 급여 합을 구한 뒤,
하루씩 이동하면서 새로 포함되는 값을 더하고, 빠지는 값을 빼면 된다.

이 방식을 슬라이딩 윈도우라고 한다.

## 코드

```python
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

cnt = sum(t[:m])
res = cnt

for i in range(m, n):
    cnt += t[i]
    cnt -= t[i - m]

    res = max(cnt, res)


print(res)
```

## 코드 설명

```python
cnt = sum(t[:m])
res = cnt
```

처음 `m`일 동안의 급여 합을 구한다.
이 값을 현재 합 `cnt`와 최댓값 `res`에 저장한다.

```python
for i in range(m, n):
```

`m`번째 인덱스부터 마지막 날까지 확인한다.

```python
cnt += t[i]
cnt -= t[i - m]
```

새로 포함되는 급여를 더하고,
윈도우에서 빠지는 급여를 뺀다.

```python
res = max(cnt, res)

```

현재 구간의 합이 기존 최댓값보다 크면 갱신한다.

## 시간복잡도

처음 합을 구하는 데 `O(m)`,
이후 배열을 한 번 순회하므로 전체 시간복잡도는 `O(n)`이다.

## 핵심 개념

* 슬라이딩 윈도우
* 연속 구간 합
* 최댓값 갱신
