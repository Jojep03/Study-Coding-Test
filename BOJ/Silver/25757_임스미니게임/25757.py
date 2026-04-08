import sys

input = sys.stdin.readline

n, game = input().split()
n = int(n)
players = []
for _ in range(n):
    player = input().strip()
    players.append(player)

players = set(players)

if game == "Y":
    print(len(players))

elif game == "F":
    print(len(players) // 2)

elif game == "O":
    print(len(players) // 3)