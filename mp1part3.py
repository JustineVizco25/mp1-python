def fitness_tracker_system():
    steps = 0
    while True:
        print("\n--- Fitness Tracker ---")
        print("1. Add Steps")
        print("2. View Total Steps")
        print("3. View Calories Burned")
        print("4. Exit to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add = input("How many steps? ")
            if not add.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            steps += int(add)
            print(f"{add} steps added!")
        elif choice == '2':
            print(f"Total Steps: {steps}")
        elif choice == '3':
            calories = steps * 0.04
            print(f"Calories Burned: {calories:.2f} calories")
        elif choice == '4':
            print("Keep moving! Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")