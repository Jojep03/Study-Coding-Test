import os
from openpyxl import Workbook

BASE_DIR = r"C:\Users\jose1\pycharmproject\Study-Coding-Test\BOJ"

wb = Workbook()
ws = wb.active
ws.title = "BOJ 문제 정리"

ws.append(["단계", "번호", "문제", "풀이여부", "복습여부"])

for tier in os.listdir(BASE_DIR):
    tier_path = os.path.join(BASE_DIR, tier)

    if not os.path.isdir(tier_path):
        continue

    for folder in os.listdir(tier_path):
        folder_path = os.path.join(tier_path, folder)

        if not os.path.isdir(folder_path):
            continue

        # 예: 1158_요세푸스문제
        if "_" in folder:
            number, title = folder.split("_", 1)
            number = int(number)
        else:
            number = folder
            title = ""

        # 문제 이름에서 '문제' 제거하고 싶으면
        #title = title.replace("문제", "")

        readme_path = os.path.join(folder_path, "README.md")
        solved = "O" if os.path.exists(readme_path) else "X"

        review = "X"
        for item in os.listdir(folder_path):
            if item.startswith(f"{number}_복습"):
                review = "O"
                break

        ws.append([tier, number, title, solved, review])

wb.save("boj_문제정리.xlsx")

print("엑셀 생성 완료!")





