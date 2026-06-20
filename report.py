import json

with open("transactions.json") as f:
    transactions = json.load(f)

category_totals = {}
total_expenses = 0

for i in transactions:
    tx_type = i["type"]
    month = i["date"][5:7]

    # Only include expense transactions
    if tx_type != "expense":
        continue

    # Only include transactions from May
    if month != "05":
        continue
    
    category = i.get("category", "uncategorized")
    amount = i["amount"]
    total_expenses += amount

    if category in category_totals:
        category_totals[category] += amount

    else:
        category_totals[category] = amount


for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{category:<15} {total:>8.2f}")
print(f"total expenses: {total_expenses:>8.2f}")

