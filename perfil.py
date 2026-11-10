# profile information

name = input("What is your name?: ")
goal = input("What is your goal?: ")
study_hours = int(input("How many hours do you study per week?: "))

monthly_hours = study_hours * 4

# my profile
print("\n=====My Profile=====")

print(f"name: {name}")
print(f"goal: {goal}")
print(f"study hours per week: {study_hours}")
print(f"study hours per month: {monthly_hours}")