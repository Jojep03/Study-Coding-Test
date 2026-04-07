import sys

input = sys.stdin.readline

while True:
    x = input().strip()

    if x == "end":
        break

    has_vowel = False
    for c in x:
        if c in "aeiou":
            has_vowel = True
            break

    ok = True
    for i in range(len(x) - 2):
        if ((x[i] in "aeiou") and (x[i + 1] in "aeiou") and (x[i + 2] in "aeiou")) or ((x[i] not in "aeiou") and (x[i + 1] not in "aeiou") and (x[i + 2] not in "aeiou")):
            ok = False
            break

    ok2 = True
    for i in range(len(x) - 1):
        if x[i] == x[i + 1] and x[i] not in "eo":
              ok2 = False
              break

    if has_vowel and ok and ok2:
        print(f"<{x}> is acceptable.")
    else:
        print(f"<{x}> is not acceptable.")

