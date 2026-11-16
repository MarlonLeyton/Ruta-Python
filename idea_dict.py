# 1. We create a list named 'ideas' containing two dictionaries
ideas = [
    {"title": "Daily news bot", "priority": "5", "status": "pending"},
    {"title": "Automated trading log", "priority": "3", "status": "In progress"}
]

print(ideas[0]["title"])

print("\n--- Listing all ideas ---")


for idea in ideas:
    print(f"{idea['title']} ({idea['priority']})")