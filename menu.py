choice = ""

while choice != "3":
    print("\n1. Add idea")
    print("2. List ideas")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding ideas...")
    elif choice == "2":
        print("Listing idea")
    elif choice == "3":
        print("Exiting")
    else:
        print("Invalid option")