def show_menu():
    print ("==== Menu ====")
    print ("Add idea")
    print ("List ideas")
    print ("Search")
    print ("Mark as done")
    print ("Exit")

def is_valid_priority(value):
    return 1 <= value <= 5
print(is_valid_priority(0))
print(is_valid_priority(9))

def format_idea(idea):
    return f"{idea['title']} | Priority: {idea['priority']} | Status: {idea['status']}"


show_menu()
idea = {"title": "bot", "priority": 4, "status": "pending"}
print(format_idea(idea))