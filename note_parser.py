import json
from datetime import date, datetime

with open("note.txt") as f:
    text = f.read()

lines = text.split('\n')

tasks = []
counter = 0

for line in lines:
    if line.startswith("- ") or line.startswith("* "):
        tasks.append(line.strip("-* "))
        counter += 1

for task in tasks: 
    print()  # Add a blank line between tasks
    print(task)

print(f"total tasks: {counter}")