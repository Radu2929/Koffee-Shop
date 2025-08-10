import mysql.connector               # Module to connect to MySQL
from tabulate import tabulate        # Module to format tables in text

def display_menu():
    """
    Ask the user which menu (books, drinks, or sweets) to display,
    fetch all rows from that table, and print them in a nice table.
    """
    # Define which table names are allowed
    valid_menus = {'books', 'drinks', 'sweets'}
    
    # Prompt the user and clean their input
    choice = input("Select menu (books, drinks or sweets): ").strip().lower()
    
    # Validate the choice
    if choice not in valid_menus:
        print(f" '{choice}' is not a valid menu. Please choose from {', '.join(valid_menus)}.")
        return  # Exit the function early if the input is invalid

    # Attempt to connect to the database
    try:
        conn = mysql.connector.connect(
            host="192.168.0.139",    # Your VM's IP address
            user="jakiea",        # Your MySQL username
            password="jakiea",# Your MySQL password
            database="koffee_shop_db"# Name of your database
        )
        cursor = conn.cursor()      # Create a cursor to perform queries

        # Execute the SQL query to get all rows from the chosen table
        cursor.execute(f"SELECT * FROM {choice}")

        # Fetch all returned rows as a list of tuples
        rows = cursor.fetchall()

        # Retrieve column names from cursor metadata
        headers = [desc[0] for desc in cursor.description]

        # Print a header to show which menu we're displaying
        print(f"\n— Showing the '{choice}' menu —")

        # Use tabulate to print the rows under the headers in a grid format
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    except mysql.connector.Error as err:
        # If any database error occurs, print it for debugging
        print(" Database error:", err)

    finally:
        # Always close both cursor and connection to free resources
        try:
            cursor.close()
            conn.close()
        except NameError:
            # If connection/​cursor never opened, ignore
            pass

if __name__ == "__main__":
    # Only run display_menu() if this script is executed directly
    display_menu()