import json
from datetime import date, datetime

import os
from dotenv import load_dotenv

from anthropic import Anthropic

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")


client = Anthropic(api_key=api_key)

with open("note.txt") as f:
    text = f.read()

prompt = f"""Extract all the to-do tasks from this daily note.
Return ONLY a valid JSON array, with no other text, no explanation, and no markdown code fences.
Each element must be an object with exactly two fields:
- "title": the task text, cleaned up
- "due": any date or time mentioned for the task, or null if none. Ignore journaling and random thoughts.

Note:
{text}"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.content[0].text)
task_json = response.content[0].text


cleaned = task_json.strip()                          # remove leading/trailing whitespace
if cleaned.startswith("```"):
    cleaned = cleaned.removeprefix("```json").removeprefix("```")  # drop opening fence
    cleaned = cleaned.removesuffix("```")             # drop closing fence
    cleaned = cleaned.strip()                          # tidy leftover whitespace

tasks = json.loads(cleaned)

# lines = text.split('\n')

# tasks = []
# counter = 0

# for line in lines:
#     if line.startswith("- ") or line.startswith("* "):
#         tasks.append(line.strip("-* "))
#         counter += 1

# for task in tasks: 
#     print()  # Add a blank line between tasks
#     print(task)

# print(f"total tasks: {counter}")

print(tasks)