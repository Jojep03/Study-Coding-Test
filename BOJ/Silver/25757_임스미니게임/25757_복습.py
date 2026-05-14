import sys

input = sys.stdin.readline

n, game = input().split()
n = int(n)
players = set()
for _ in range(n):
    player = input().strip()
    players.add(player)

if game == "Y":
    print(len(players))
elif game == "F":
    print(len(players) // 2)
elif game == "O":
    print(len(players) // 3)

