import json
from datetime import date, datetime

with open("tasks.json") as f:
    tasks = json.load(f)

# print(tasks)

today = date.today()

no_date = []
overdue = []
today_tasks = []
upcoming = []

for i in tasks:
    title = i["title"]
    due_date = i.get("due", "no due date")

    if due_date == "no due date":
        no_date.append(i)
        continue
    
    due_obj = datetime.strptime(due_date, "%Y-%m-%d").date()

    if due_obj < today:
        overdue.append(i)
    elif due_obj == today:
        today_tasks.append(i)
    else:
        upcoming.append(i)

print("\nToday's tasks:")
for task in today_tasks:
    print(f"{task['title']: <25}, {task['due']: >10}")

print("\nOverdue tasks:")
for task in overdue:
    print(f"{task['title']: <25}, {task['due']: >10}")

print("\nUpcoming tasks:")
for task in upcoming:
    print(f"{task['title']: <25}, {task['due']: >10}")

print("\nTasks with no due date:")
for task in no_date:
    print(f"{task['title']: <25}, has no date")

