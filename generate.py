import csv
import random
import os
import sys

NUM_ROWS = 50
COLUMNS = ["Фамилия", "Регион", "Сумма продаж", "Процент с продаж"]

def generate_row():
    sales = random.randint(2000, 100000)
    return {
        "Фамилия": random.choice(["Лобанов", "Микаэлян", "Мартынов", "Баринов", "Джекович"]),
        "Регион": random.choice(["Сахалин", "Москва", "Саратов", "Пятигорск", "Омск"]),
        "Сумма продаж": sales,
        "Процент с продаж": round(sales * 0.2, 2),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)