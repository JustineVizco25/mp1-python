def restaurant_order_system():
    total = 0
    while True:
        print("\n--- Python Restaurant ---")
        print("1. Burger - ₱120")
        print("2. Pizza  - ₱300")
        print("3. Pasta  - ₱250")
        print("4. Fries  - ₱80")
        print("5. Exit to Main Menu")
        choice = input("Select an item: ")

        if choice == '1':
            total += 120
            print("Added Burger to your order.")
        elif choice == '2':
            total += 300
            print("Added Pizza to your order.")
        elif choice == '3':
            total += 250
            print("Added Pasta to your order.")
        elif choice == '4':
            total += 80
            print("Added Fries to your order.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    print("\n--- Order Summary ---")
    print(f"Total before discount: ₱{total}")
    if total > 500:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: ₱{discount:.2f}")
    print(f"Final Amount to Pay: ₱{total:.2f}\n")


def grocery_store_system():
    # Prices
    PRICE_RICE = 50
    PRICE_EGGS = 7
    PRICE_MILK = 60
    PRICE_BREAD = 35

    # Quantities
    rice_qty = 0
    eggs_qty = 0
    milk_qty = 0
    bread_qty = 0

    while True:
        print("\n--- Grocery Store ---")
        print("1. View Items")
        print("2. Add to Cart")
        print("3. Checkout")
        print("4. Exit to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            print(f"Rice: ₱{PRICE_RICE}, Eggs: ₱{PRICE_EGGS}, Milk: ₱{PRICE_MILK}, Bread: ₱{PRICE_BREAD}")
        elif choice == '2':
            item = input("Enter item to add (Rice/Eggs/Milk/Bread): ")
            qty = input("Enter quantity: ")
            if not qty.isdigit():
                print("Invalid quantity. Please enter a number.")
                continue
            qty = int(qty)

            if item.lower() == 'rice':
                rice_qty += qty
            elif item.lower() == 'eggs':
                eggs_qty += qty
            elif item.lower() == 'milk':
                milk_qty += qty
            elif item.lower() == 'bread':
                bread_qty += qty
            else:
                print("Item not available.")
                continue

            print(f"Added {qty} {item}(s) to cart.")
        elif choice == '3':
            subtotal = (rice_qty * PRICE_RICE + eggs_qty * PRICE_EGGS +
                        milk_qty * PRICE_MILK + bread_qty * PRICE_BREAD)
            vat = subtotal * 0.12
            total = subtotal + vat

            print("\n--- Cart Summary ---")
            if rice_qty:
                print(f"Rice x {rice_qty} = ₱{rice_qty * PRICE_RICE}")
            if eggs_qty:
                print(f"Eggs x {eggs_qty} = ₱{eggs_qty * PRICE_EGGS}")
            if milk_qty:
                print(f"Milk x {milk_qty} = ₱{milk_qty * PRICE_MILK}")
            if bread_qty:
                print(f"Bread x {bread_qty} = ₱{bread_qty * PRICE_BREAD}")

            print(f"\nSubtotal: ₱{subtotal}")
            print(f"VAT (12%): ₱{vat:.2f}")
            print(f"Total: ₱{total:.2f}\n")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


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


def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Python Restaurant")
        print("2. Grocery Store")
        print("3. Fitness Tracker")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            restaurant_order_system()
        elif choice == '2':
            grocery_store_system()
        elif choice == '3':
            fitness_tracker_system()
        elif choice == '4':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
