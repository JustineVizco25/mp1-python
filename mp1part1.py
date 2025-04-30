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

