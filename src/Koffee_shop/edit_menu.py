import mysql.connector  # This library lets Python talk to MySQL

# This function connects to your MySQL database
def get_connection():
    return mysql.connector.connect(
        host="192.168.0.139",        # Change this to your VM or database host
        user="your_user",            # Your MySQL username
        password="your_password",    # Your MySQL password
        database="koffee_shop_db"    # The name of your database
    )

# Ask the user which menu (table) they want to work with
def choose_menu():
    menus = ['books', 'drinks', 'sweets']
    choice = input("Choose a menu (books, drinks, or sweets): ").strip().lower()
    
    # Check if the user's choice is valid
    if choice not in menus:
        print(" Invalid menu choice.")
        return None  # Exit if not valid
    return choice

# Add a new item to the chosen menu
def insert_item(menu):
    conn = get_connection()
    cursor = conn.cursor()  # Used to send commands to the database

    # Ask for item details based on the menu
    if menu == "books":
        name = input("Book name: ")
        genre = input("Genre: ")
        author = input("Author: ")
        price = float(input("Price: "))
        stock = int(input("Total stock: "))

        # SQL command to insert a new book
        sql = "INSERT INTO books (name, genre, author, price, total_stock) VALUES (%s, %s, %s, %s, %s)"
        values = (name, genre, author, price, stock)

    elif menu == "drinks":
        name = input("Drink name: ")
        price = float(input("Price: "))
        calories = int(input("Calories: "))
        stock = int(input("Total stock: "))

        # SQL command to insert a new drink
        sql = "INSERT INTO drinks (name, price, calories, total_stock) VALUES (%s, %s, %s, %s)"
        values = (name, price, calories, stock)

    elif menu == "sweets":
        name = input("Sweet name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        flavour = input("Flavour: ")
        stock = int(input("Total stock: "))
        calories = int(input("Calories: "))

        # SQL command to insert a new sweet
        sql = "INSERT INTO sweets (name, category, price, flavour, total_stock, calories) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, category, price, flavour, stock, calories)

    # Run the SQL command with the given values
    cursor.execute(sql, values)
    conn.commit()  # Save changes to the database

    print(" Item added successfully.")

    cursor.close()
    conn.close()  # Close the connection when done

# Delete an item by its name
def delete_item(menu):
    name = input("Enter the name of the item to delete: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    # SQL command to delete an item where the name matches
    sql = f"DELETE FROM {menu} WHERE name = %s"
    cursor.execute(sql, (name,))
    conn.commit()

    # Check if any row was actually deleted
    if cursor.rowcount > 0:
        print(" Item deleted.")
    else:
        print(" Item not found.")

    cursor.close()
    conn.close()

# Update an item's price and stock by its name
def update_item(menu):
    name = input("Enter the name of the item to update: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    # Check if item exists
    cursor.execute(f"SELECT * FROM {menu} WHERE name = %s", (name,))
    if cursor.fetchone() is None:
        print(" Item not found.")
        cursor.close()
        conn.close()
        return

    # Ask user what to change
    new_price = float(input("New price: "))
    new_stock = int(input("New stock: "))

    # Update query for each menu
    if menu == "books":
        sql = "UPDATE books SET price = %s, total_stock = %s WHERE name = %s"
    elif menu == "drinks":
        sql = "UPDATE drinks SET price = %s, total_stock = %s WHERE name = %s"
    elif menu == "sweets":
        sql = "UPDATE sweets SET price = %s, total_stock = %s WHERE name = %s"

    values = (new_price, new_stock, name)

    cursor.execute(sql, values)
    conn.commit()

    print(" Item updated.")

    cursor.close()
    conn.close()

# Main menu that lets the user choose what to do
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Insert new item")
        print("2. Update existing item")
        print("3. Delete item")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ").strip()

        # Exit the program
        if choice == '4':
            print("Goodbye!")
            break

        # Ask user which table to use
        menu = choose_menu()
        if not menu:
            continue  # Go back to menu if input was invalid

        # Run the correct function
        if choice == '1':
            insert_item(menu)
        elif choice == '2':
            update_item(menu)
        elif choice == '3':
            delete_item(menu)
        else:
            print(" Invalid choice. Try again.")

# Only run the main program if this file is being executed directly
if __name__ == "__main__":
    main()
