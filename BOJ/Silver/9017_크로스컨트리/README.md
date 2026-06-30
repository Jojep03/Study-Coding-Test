# [백준 9017번] 크로스 컨트리 - Python

## 문제 설명

크로스 컨트리 경기는 결승선을 통과한 순서대로 점수가 부여된다.

하지만 모든 팀이 점수 계산에 포함되는 것은 아니다.

한 팀에서 **정확히 6명의 선수**가 참가한 팀만 점수 계산에 포함된다.
6명이 아닌 팀의 선수들은 순위에서 제외하고, 남은 선수들끼리 다시 점수를 매긴다.

각 팀의 점수는 해당 팀에서 먼저 들어온 **상위 4명의 점수 합**으로 계산한다.

점수가 가장 낮은 팀이 우승하며, 점수가 같다면 **5번째 선수의 점수**가 더 낮은 팀이 우승한다.

## 문제 풀이

핵심은 먼저 **6명이 참가한 팀만 남기는 것**이다.

예를 들어 결승선을 통과한 순서가 다음과 같다고 하자.

```text
1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
```

각 팀의 참가 인원을 세어 보면,

```text
1번 팀: 6명
2번 팀: 2명
3번 팀: 6명
4번 팀: 1명
```

따라서 1번 팀과 3번 팀만 점수 계산에 포함된다.

2번 팀과 4번 팀 선수들은 제외하고 다시 순위를 매긴다.

```text
1 3 3 1 3 1 1 3 1 3 3 1
```

이제 이 순서대로 1점, 2점, 3점, ... 을 부여한다.

각 팀마다 필요한 정보는 다음과 같다.

```text
[현재까지 들어온 선수 수, 상위 4명 점수 합, 5번째 선수 점수]
```

상위 4명의 점수 합이 가장 낮은 팀이 이기고,
점수가 같다면 5번째 선수 점수가 더 낮은 팀이 이긴다.

## 코드

```python
import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    players = list(map(int, input().split()))

    counter = Counter(players)

    y = []
    for player in players:
        if counter[player] == 6:
            y.append(player)

    lst = {}
    idx = 1

    for player in y:
        if player in lst:
            if lst[player][0] < 4:
                lst[player][0] += 1
                lst[player][1] += idx
            elif lst[player][0] == 4:
                lst[player][0] += 1
                lst[player][2] = idx
        else:
            lst[player] = [1, idx, 0]

        idx += 1

    lst = sorted(lst.items(), key=lambda x: (x[1][1], x[1][2]))

    print(lst[0][0])
```

## 코드 설명

```python
counter = Counter(players)
```

각 팀 번호가 몇 번 등장했는지 센다.
즉, 각 팀의 참가 선수 수를 구한다.

```python
y = []
for player in players:
    if counter[player] == 6:
        y.append(player)
```

참가 선수가 정확히 6명인 팀의 선수만 `y`에 넣는다.

6명이 아닌 팀의 선수들은 점수 계산에서 제외된다.

```python
lst = {}
idx = 1
```

`lst`는 팀별 점수 정보를 저장하는 딕셔너리이다.
`idx`는 유효한 선수들끼리 다시 매긴 점수이다.

```python
for player in y:
```

점수 계산에 포함되는 선수들을 순서대로 확인한다.

```python
if player in lst:
```

이미 한 번 이상 등장한 팀이라면 기존 정보를 수정한다.

```python
if lst[player][0] < 4:
    lst[player][0] += 1
    lst[player][1] += idx
```

해당 팀에서 아직 4명 이하의 선수가 들어온 경우이다.

상위 4명의 점수 합에 현재 점수 `idx`를 더한다.

```python
elif lst[player][0] == 4:
    lst[player][0] += 1
    lst[player][2] = idx
```

해당 팀의 5번째 선수가 들어온 경우이다.

5번째 선수의 점수는 동점일 때 비교해야 하므로 따로 저장한다.

```python
else:
    lst[player] = [1, idx, 0]
```

해당 팀이 처음 등장한 경우이다.

첫 번째 선수는 상위 4명에 포함되므로 점수 합에 `idx`를 넣는다.

리스트의 의미는 다음과 같다.

```text
[현재까지 들어온 선수 수, 상위 4명 점수 합, 5번째 선수 점수]
```

```python
idx += 1
```

다음 선수에게 줄 점수를 1 증가시킨다.

```python
lst = sorted(lst.items(), key=lambda x: (x[1][1], x[1][2]))
```

팀들을 정렬한다.

정렬 기준은 다음과 같다.

```text
1. 상위 4명 점수 합이 낮은 팀
2. 점수가 같다면 5번째 선수 점수가 낮은 팀
```

```python
print(lst[0][0])
```

정렬 후 가장 앞에 있는 팀 번호가 우승 팀이므로 출력한다.

## 예제

입력:

```text
2
15
1 2 3 3 1 3 2 4 1 1 3 1 3 3 1
18
1 2 3 1 2 3 1 2 3 3 3 3 2 2 2 1 1 1
```

출력:

```text
1
3
```

## 정리

이 문제는 단순히 들어온 순서대로 점수를 계산하는 문제가 아니라,
먼저 **정확히 6명이 참가한 팀만 골라내야 하는 문제**이다.

6명이 아닌 팀은 순위에서 제외하고, 남은 선수들끼리 다시 점수를 매긴다.

그 후 각 팀의 상위 4명 점수 합을 비교하고,
동점이면 5번째 선수 점수로 우승 팀을 결정하면 된다.
