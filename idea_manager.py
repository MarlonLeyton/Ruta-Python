ideas = []

# Part A: ask for the title until it is not empty
while True:
    title = input("What is the title?: ").strip()
    
    if title != "":
        break
    print("The title cannot be empty. Please try again.")

# Part B: ask for priority using .isdigit() until it is a valid number from 1 to 5
while True:
    priority_input = input("What level of priority will it have from 1 to 5?: ").strip()
    
    if priority_input.isdigit():
        priority = int(priority_input)
        if 1 <= priority <= 5:
            break
        print("Invalid priority. Please enter a number between 1 and 5.")
    else:
        print("Please enter a valid integer number.")

# Part C: create the dictionary and add it to the ideas list
new_idea = {
    "title": title,
    "priority": priority,
    "status": "pending"
}

ideas.append(new_idea)

print("\n==== Idea Successfully Saved! ====")
print(ideas)