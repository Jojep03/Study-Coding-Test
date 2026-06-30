import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    players = list(map(int, input().split()))
    x = set()
    y = []
    # for player in players:
    #     if players.count(player) == 6:
    #         x.add(player)
    #         y.append(player)
    counter = Counter(players)
    # print(counter)
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