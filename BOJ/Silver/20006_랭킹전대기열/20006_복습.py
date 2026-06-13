import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rooms = []
for _ in range(n):
    lev, name = input().split()
    lev = int(lev)

    enter = False
    for room in rooms:
        host_l = room[0][0]
        if len(room) < m and abs(host_l - lev) <= 10:
            room.append((lev, name))
            enter = True
            break
    if not enter:
        rooms.append([(lev, name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for level, name in sorted(room, key=lambda x: x[1]):
        print(level, name)