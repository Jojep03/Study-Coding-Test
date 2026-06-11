import sys

input = sys.stdin.readline

# while True:
#     t = input().strip()
#     check_1 = False
#     check_2 = True
#     check_3 = True
#     if t == "end":
#         break
#     for x in t:
#         if x in "aeiou":
#             check_1 = True
#             break
#     for i in range(len(t) - 2):
#         if ((t[i] in "aeiou") and (t[i + 1] in "aeiou") and (t[i + 2] in "aeiou")) or ((t[i] not in "aeiou") and (t[i + 1] not in "aeiou") and (t[i + 2] not in "aeiou")):
#             check_2 = False
#             break
#     for i in range(len(t) - 1):
#         if t[i] == t[i + 1] and t[i] not in "eo":
#             check_3 = False
#             break
#     if check_1 and check_2 and check_3:
#         print(f"<{t}> is acceptable.")
#     else:
#         print(f"<{t}> is not acceptable.")

vowels = "aeiou"

while True:
    t = input().strip()
    if t == "end":
        break

    check_1 = any(x in vowels for x in t)
    check_2 = True
    check_3 = True

    for i in range(len(t) - 2):
        if (t[i] in vowels) == (t[i + 1] in vowels) == (t[i + 2] in vowels):
            check_2 = False
            break

    for i in range(len(t) - 1):
        if t[i] == t[i + 1] and t[i] not in "eo":
            check_3 = False
            break

    if check_1 and check_2 and check_3:
        print(f"<{t}> is acceptable.")
    else:
        print(f"<{t}> is not acceptable.")