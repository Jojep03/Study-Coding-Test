# BOJ 1260 DFS와 BFS

문제 링크  
https://www.acmicpc.net/problem/1260

---

## 문제 설명

그래프가 주어졌을 때 **DFS(Depth First Search)**와 **BFS(Breadth First Search)**를 수행한 결과를 출력하는 문제이다.

조건

- 시작 정점은 `V`
- 방문할 수 있는 정점이 여러 개라면 **번호가 작은 정점부터 방문**
- 그래프는 **무방향 그래프**

---

## 알고리즘

- DFS (Depth First Search)
- BFS (Breadth First Search)

---

## 풀이 아이디어

그래프 탐색 문제이므로 인접 리스트 형태로 그래프를 구성한 뒤 DFS와 BFS를 구현한다.

### 1. 무방향 그래프 처리

입력으로 주어지는 간선 `(x, y)`는 양방향으로 이동 가능하다.

```python
graph[x].append(y)
graph[y].append(x)
```

### 2. 작은 번호부터 방문하기 위해 정렬

문제 조건에 따라 정점 번호가 작은 것부터 방문해야 하므로
각 정점의 인접 리스트를 정렬한다.

```python
for i in range(1, n + 1):
    graph[i].sort()
```

### 3. DFS 구현

DFS는 **스택(Stack)**을 사용하여 구현하였다.

스택은 LIFO (Last In First Out) 구조이기 때문에
작은 번호부터 방문하려면 큰 번호부터 스택에 넣어야 한다.

따라서 reversed()를 사용한다.

```python
for nxt in reversed(graph[node]):
```

### 4. BFS 구현

BFS는 **큐(Queue)**를 사용한다.

큐는 FIFO (First In First Out) 구조이므로
정렬된 순서 그대로 큐에 넣으면 자연스럽게 작은 번호부터 방문하게 된다.

```python
for nxt in graph[node]:
```

### 시간 복잡도

DFS와 BFS 모두 모든 정점과 간선을 한 번씩 확인한다.

```python
O(N + M)
```

| 탐색  | 자료구조  |    특징 |
|-----|:-----:|------:|         
| DFS | Stack | 깊이 우선 |
| BFS | Queue | 너비 우선 |

DFS에서는 ***스택 특성 때문에 reversed 필요***,

BFS에서는 ***큐 특성 때문에 reversed 필요 없음***.