import requests
import random

URL = "http://127.0.0.1:8000/books/"

for i in range(200):
    data = {
        "title": f"Book {i}",
        "author": random.choice(["Orwell", "Tolkien", "Rowling"]),
        "year": random.randint(1950, 2023),
        "extra": {
            "genre": random.choice(["fantasy", "drama", "sci-fi"]),
            "pages": random.randint(100, 800)
        }
    }
    requests.post(URL, json=data)

print("DB populated")
