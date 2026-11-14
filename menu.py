choice = ""
ideas = []

while choice != "3":
    print("\n1. Add idea")
    print("2. List ideas")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding ideas...")
        title = input("Enter your idea: ")
        ideas.append(title)
        print(f"Idea '{title}', saved successfully")
    elif choice == "2":
        if len(ideas) == 0:
            print("No ideas yet")
        else:
            for number, idea in enumerate(ideas, start=1):
                print(f"{number}. {idea}")

    elif choice == "3":
        print("Exiting")
    else:
        print("Invalid option")