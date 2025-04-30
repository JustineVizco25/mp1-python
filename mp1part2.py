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