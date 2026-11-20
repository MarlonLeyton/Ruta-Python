# Idea Manager v0.2 (refactored with functions)


def show_menu():
    print("\n==== Menu ====")
    print("1. Add idea")
    print("2. List ideas")
    print("3. Search")
    print("4. Mark as done")
    print("5. Exit")


def is_valid_priority(value):
    return 1 <= value <= 5


def add_idea(ideas):
    while True:
        title = input("What is the title?: ").strip()

        if title != "":
            break
        print("The title cannot be empty. Please try again.")

    while True:
        priority_input = input("What level of priority will it have from 1 to 5?: ").strip()

        if priority_input.isdigit():
            priority = int(priority_input)
            if is_valid_priority(priority):
                break
            print("Invalid priority. Please enter a number between 1 and 5.")
        else:
            print("Please enter a valid integer number.")

    new_idea = {
        "title": title,
        "priority": priority,
        "status": "pending"
    }

    ideas.append(new_idea)
    print("\n==== Idea Successfully Saved! ====")


def list_ideas(ideas):
    if len(ideas) == 0:
        print("\nNo ideas yet")
    else:
        print("\n==== Your ideas ====")
        for number, idea in enumerate(ideas, start=1):
            print(f"{number}. {idea['title']} | Priority: {idea['priority']} | Status: {idea['status']}")


def search_ideas(ideas):
    keyword = input("Search for: ").strip().lower()

    if keyword == "":
        print("\nPlease type a word to search.")
    else:
        found = False
        for idea in ideas:
            if keyword in idea["title"].lower():
                print(f"- {idea['title']} | Priority: {idea['priority']} | Status: {idea['status']}")
                found = True

        if not found:
            print("\nNo matches")


def mark_done(ideas):
    if len(ideas) == 0:
        print("\nNo ideas yet")
    else:
        for number, idea in enumerate(ideas, start=1):
            print(f"{number}. {idea['title']} | Status: {idea['status']}")

        number_input = input("Number of the idea to mark as done: ").strip()

        if number_input.isdigit() and 1 <= int(number_input) <= len(ideas):
            position = int(number_input) - 1
            ideas[position]["status"] = "done"
            print(f"\n'{ideas[position]['title']}' is now done!")
        else:
            print("\nInvalid number.")


ideas = []
choice = ""

while choice != "5":
    show_menu()

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_idea(ideas)
    elif choice == "2":
        list_ideas(ideas)
    elif choice == "3":
        search_ideas(ideas)
    elif choice == "4":
        mark_done(ideas)
    elif choice == "5":
        print("\nGoodbye!")
    else:
        print("\nInvalid option. Please choose a number from 1 to 5.")