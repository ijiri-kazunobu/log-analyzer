import random
from datetime import datetime, timedelta

random.seed(42)

LEVELS = ["INFO"] * 6 + ["WARN"] * 2 + ["ERROR"]
MESSAGES = {
    "INFO": ["request completed", "user login", "cache hit"],
    "WARN": ["slow query", "high memory usage"],
    "ERROR": ["db connection failed", "timeout", "file not found"],
}
MODULES = ["api", "db", "auth", "cache"]

t = datetime(2026, 10, 18, 9, 0, 0)
for _ in range(200):
    t += timedelta(seconds=random.randint(1, 60))
    level = random.choice(LEVELS)
    msg = random.choice(MESSAGES[level])
    print(f"{t:%Y-%m-%d %H:%M:%S} {level} [{random.choice(MODULES)}] {msg}")
