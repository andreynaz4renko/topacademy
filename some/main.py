import json
from random import choice
from faker import Faker
fake = Faker()

categories = ['Гонки'.encode("utf-8"), 'Стратегии'.encode("utf-8"), 'Симуляторы'.encode("utf-8")]

f = open("C:/Users/andy/Desktop/index-v1.json")

data = json.load(f)

apps = data["apps"]
additional = []

for app in apps:
    additional.append(
        {
            "package": app["packageName"],
            "age_rating": fake.random.randint(0, 20),
            "downloads_count": 0,
            "category": choice(categories).decode("utf-8"),
            "rating": float(str(fake.random.random() * 5)[:4])
        }
    )

print(json.dumps(additional, indent=2))