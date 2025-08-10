# - Display a list of the menu and book items (Employees/Employer)
 
from menudictionary import drinks, books, sweets
 
all_menu = [sweets, drinks, books]  # 3 dictionaries in a list
 
def displaymenu():
    select_menu = input("Select which menu: Sweets, Drinks, Books or All ").lower()
 
    if select_menu == 'all':
        for menu in all_menu:
            for name, info in menu.items():
                print(f"\nItem Name: {name}")
                for key, value in info.items():
                    print(f"{key}: {value}")
 
    elif select_menu == 'sweets':
        for sweet, info in sweets.items():
            print(f"\nSweet: {sweet}")
            print(f"Price: {info['price']}")
            print(f"Category: {info['category']}")
            print(f"Flavour: {info['flavour']}")
            print(f"Total Stock: {info['total_stock']}")
 
    elif select_menu == 'drinks':
        for drink, info in drinks.items():
            print(f"\nDrink: {drink}")
            print(f"Price: {info['price']}")
            print(f"Type: {info['type'] if info['type'] else 'N/A'}")
            print(f"Calories: {info['calories']}")
            print(f"Total Stock: {info['total_stock']}")
            print(f"ID: {info['id']}")
 
    elif select_menu == 'books':
        for book, info in books.items():
            print(f"\nBook: {book}")
            print(f"Author: {info['author']}")
            print(f"Genre: {info['genre']}")
            print(f"Price: {info['price']}")
            print(f"Total Stock: {info['total_stock']}")
            print(f"Book ID: {info['Book ID']}")
 
    else:
        print("Invalid option. Please choose from Sweets, Drinks, Books, or All.")
 
# Run the function once, or loop it if you want multiple selections
displaymenu()