# Define dictionaries to store achieved and pending goals
achieved_goals = {}
pending_goals = {}

# Function to add new goal/s
def add_goal():
    goal_name = input("Enter your goal/s: ")
    goal_description = input("Enter a description of your goal/s: ")
    pending_goals[goal_name] = goal_description
    print(f"Goal '{goal_name}' added successfully!")
    print(f"Updated Percentage of Goals Achieved: {update_percentage():.2f}%")

# Function to view achieved and pending goal/s
def view_goals():
    print("\nAchieved Goals: ")
    for goal_name, goal_description in achieved_goals.items():
        print(f"Goal: {goal_name}")
        print(f"Description: {goal_description}")
        print("-" * 20)

    print("\nPending Goals: ")
    for goal_name, goal_description in pending_goals.items():
        print(f"Goal: {goal_name}")
        print(f"Description: {goal_description}")
        print("-" * 20)

# Function to remove goal/s
def remove_goal():
    goal_name = input("Enter the goal you want to remove: ")
    if goal_name in pending_goals:
        del pending_goals[goal_name]
        print(f"Goal '{goal_name}' removed successfully!")
        print(f"Updated Percentage of Goals Achieved: {update_percentage():.2f}%")
    elif goal_name in achieved_goals:
        del achieved_goals[goal_name]
        print(f"Goal '{goal_name}' removed successfully!")
    else:
        print(f"Goal '{goal_name}' not found.")

# Function to mark goal/s as achieved
def mark_achieved():
    goal_name = input("Enter goal/s you've achieved: ")
    if goal_name in pending_goals:
        achieved_goals[goal_name] = pending_goals[goal_name]
        del pending_goals[goal_name]
        print(f"Congratulations on achieving goal/s '{goal_name}'!")
        print(f"Updated Percentage of Goals Achieved: {update_percentage():.2f}%")
    else:
        print(f"Goal '{goal_name}' not found in your pending goals.")

# Function to calculate and display the percentage of goal/s achieved
def calculate_percentage():
    total_goals = len(pending_goals) + len(achieved_goals)
    achieved_count = len(achieved_goals)
    percentage_achieved = (achieved_count / total_goals) * 100 if total_goals > 0 else 0
    print(f"You have achieved {achieved_count} out of {total_goals} goals, which is {percentage_achieved:.2f}%.")

# Function to update the percentage of goal/s achieved
def update_percentage():
    total_goals = len(pending_goals) + len(achieved_goals)
    achieved_count = len(achieved_goals)
    percentage_achieved = (achieved_count / total_goals) * 100 if total_goals > 0 else 0
    return percentage_achieved

# Main Loop
while True:
    print("\nGoals Tracker")
    print("1. Add Goal/s")
    print("2. View Goal/s")
    print("3. Remove Goal/s")
    print("4. Mark Goal as Achieved")
    print("5. Calculate Percentage of Goals Achieved")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_goal()
    elif choice == '2':
        view_goals()
    elif choice == '3':
        remove_goal()
    elif choice == '4':
        mark_achieved()
    elif choice == '5':
        calculate_percentage()
    elif choice == '6':
        print("Program Terminated.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5/6).")
