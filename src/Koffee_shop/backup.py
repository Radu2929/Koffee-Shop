# Import the dictionaries for drinks, books, and sweets from another file
# These hold all the available items and their details
from menudictionary import drinks, books, sweets

# Group all menus into a single list for easier iteration
# This way we can loop over sweets, drinks, and books together
all_menu = [sweets, drinks, books]

# This list stores the customer's selected items
basket = []

# This dictionary will map menu numbers (as strings) to actual items and their info
numbered_items = {}

# Function to display all available items, each with a number for selection
def show_all_items():
    print("\nAvailable Items:")
    
    # Clear any previous entries before re-populating
    numbered_items.clear()

    # Start item numbering from 1
    count = 1

    # Loop over all categories (sweets, drinks, books)
    for menu in all_menu:
        # Loop through each item in the category
        for item, info in menu.items():
            # Only show items that have stock left
            if info['total_stock'] > 0:
                # Add entry to numbered_items like: {'1': ('Latte', {info})}
                numbered_items[str(count)] = (item, info)
                # Print item with its assigned number and price formatted to 2 decimal places
                print(f"{count}. {item} (${info['price']:.2f})")
                count += 1

# Function to add a selected item to the basket by number
def add_to_basket(item_number):
    # Check if the entered number corresponds to a valid item
    if item_number in numbered_items:
        # Retrieve the tuple from numbered_items based on the item_number
        item_tuple = numbered_items[item_number]
        # Example Item Tuple: ('Latte', {'price': 4.5, 'total_stock': 10})
        
        # Unpack the tuple into two separate variables
        item_name = item_tuple[0]  # First element is the item name
        item_info = item_tuple[1]  # Second element is the item info (price, stock)

        # Find the correct menu and reduce its stock count
        for menu in all_menu:
            if item_name in menu:
                menu[item_name]['total_stock'] -= 1
                break

        # Add the item to the basket
        basket.append({'name': item_name, 'price': item_info['price']})
        return True  # Confirm it was successfully added
    return False  # Invalid selection

# Function to print a receipt of all items in the basket and return total price
def show_receipt():
    print("\nReceipt:")
    total = 0  # Running total

    # Loop through all items in the basket
    for item in basket:
        print(f"- {item['name']}: ${item['price']:.2f}")
        total += item['price']  # Add item price to total

    print(f"\nTotal: ${total:.2f}")  # Print final total
    return total  # Return total for use in discount

# Function to apply employee discount after verifying credentials
def apply_employee_discount(total):
    print("\nEmployee Discount Verification")

    # Ask for credentials
    username = input("Username: ").strip().lower()  # .strip() removes extra spaces, .lower() standardizes input
    password = input("Password: ").strip()

    # Check credentials
    if username == 'tobias' and password == 'bode':
        while True:
            try:
                # Ask how much discount they want to apply
                discount_input = float(input("Enter discount percentage (max 50%): "))
                if 0 <= discount_input <= 50:
                    discount_amount = total * (discount_input / 100)  # Calculate discount value
                    discounted_total = total - discount_amount  # New total after discount
                    print(f"\nDiscount applied: {discount_input:.0f}%")
                    print(f"New Total: ${discounted_total:.2f}")
                    break
                else:
                    print("Please enter a number between 0 and 50.")
            except ValueError:
                # Handles non-numeric inputs
                print("Invalid input. Please enter a numeric value.")
    else:
        print("Invalid credentials. No discount applied.")

# Main function that controls the order process
def take_order():
    # Show the list of items to the user
    show_all_items()

    # Let customer select multiple items
    while True:
        item_number = input("\nEnter item number to add to basket (or type 'done'): ").strip()

        if item_number.lower() == 'done':
            # Exit loop when user is done ordering
            break
        elif add_to_basket(item_number):
            # If item added successfully, confirm to user
            item_name = numbered_items[item_number][0]
            print(f"{item_name} added to your basket.")
        else:
            # Handle invalid number or out-of-stock item
            print("Invalid selection or item is out of stock.")

    # Show all selected items and the total
    total = show_receipt()

    # Ask if discount should be applied
    apply_discount = input("\nApply employee discount? (yes/no): ").strip().lower()
    if apply_discount == "yes":
        apply_employee_discount(total)

take_order()