from menudictionary import item_descriptions
def view_additonal_info():
    for productcode, description in item_descriptions.items():
        print("What would you like to view information for: ")
        print("Enter 1 to view all Products")
        print("Enter 2 to filter by (Product ID)")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1": 
            for productcode, description in item_descriptions.items():
                print(f"Product ID: {productcode}")
                print(f"Description: {description}")

        elif choice == "2":
            code = input("Enter Product Code e.g D001, B001, S001")
            if code in item_descriptions:
                print(f"\nProduct ID: {productcode}")
                print(f"Description: {description}")
            else:
                print("Product Code not found")

        elif choice == "done":
            break

        else:
            print("Invalid Selection. Please enter 1 or 2.")

view_additonal_info()







# while True:
#     choice = input("\nEnter the name of the item you want to order (or type 'done' to finish): ").lower()

#     if choice.startswith("details ") or choice.startswith("tell me about "):
#         item_query = choice.replace("details ", "").replace("tell me about ", "").strip()
#         if item_query in item_descriptions:
#             print("\n" + item_descriptions[item_query])
#         else:
#             print("Sorry, I don't have details for that item.")
#         continue

#     if choice == 'done':
#         break
#     elif choice not in item_descriptions:
#         print("Sorry, that item is not on the menu.")
#         continue
