import sys

p, m = map(int, input().split())

rooms = []
for _ in range(p):
    l, n = input().split()
    l = int(l)

    enter = False

    for room in rooms:
        host_level = room[0][0]
        if len(room) < m and abs(host_level - l) <= 10:
            room.append((l, n))
            enter = True
            break

    if not enter:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print("Strated!")

    else:
        print("Waiting!")

    for level, name in sorted(room, key=lambda x: x[1]):
        print(level, name)

