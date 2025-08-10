
# This Python application simulates an interactive ordering system for a small café and bookstore. 
# It allows users to browse a categorised menu of drinks, sweets, and books, add items to a virtual 
# basket, and receive a detailed receipt at checkout. The program includes inventory tracking to 
# prevent overselling, as well as a secure employee login feature to apply staff discounts. Designed
#  to run in a command-line interface, this project demonstrates key programming concepts such as 
# dictionaries, control flow, user input handling, and modular function design—all wrapped in a 
# real-world retail use case.



drinks = {    
    'Latte': {
        "type": "",
        "total_stock": 0,
        "price": 2.50,
        "calories": 125,
        "id": 'D001'
    },    
    "cappucino": {
        "type": "", 
        "total_stock": 25,
        "price": 3.00,
        "calories": 225,
        "id": 'D002'
    }, 
    'espresso': {
        "type": "",
        "total_stock": 25,
        "price": 1.50,
        "calories": 25,
        "id": 'D003'
    }
}

books = {
    "Lord of the Rings" : {
            "genre": "Thriller",
            "author": "J.R.R. Tolkien",
            "price": 8.99,
            "total_stock": 20,
            "Book ID": "B001"
        },
        "A Brief History of Time": {
            "genre": "Science",
            "author": "Stephen Hawking",
            "price": 10.50,
            "total_stock": 15,
            "Book ID": "B002"
        },
        "Pride and Prejudice": {
            "genre": "Romance",
            "author": "Jane Austen",
            "price": 6.75,
            "total_stock": 25,
            "Book ID": "B003"
        }
}

sweets = {
    "Chocolate Chip Cookie": {
        "category": "Cookie",
        "price": 1.50,
        "flavour": "Chocolate Chip",
        "total_stock": 30,
        "calories": 180,
        "id": 'S001'
    },
    "Fudge Brownie": {
        "category": "Brownie",
        "price": 2.00,
        "flavour": "Double Chocolate",
        "total_stock": 25,
        "calories": 250,
        "id": 'S002'
    },
    "Classic Cinnamon Roll": {
        "category": "Cinnamon Roll",
        "price": 2.75,
        "flavour": "Cinnamon & Sugar",
        "total_stock": 20,
        "calories": 320,
        "id": 'S003'
    }
}

item_descriptions = {
    "D001": "Latte\nA traditional latte consists of one or two shots of espresso combined with steamed milk and finished with a thin layer of frothed milk. Popularized in the United States during the 1980s, the modern latte has become a staple in coffee culture.",
    
    "D002": "Cappuccino\nAn Italian classic with equal parts espresso, steamed milk, and milk foam. It’s rich, bold, and velvety smooth.",
    
    "D003": "Espresso\nA strong and concentrated coffee shot, perfect for those who enjoy a robust and intense coffee flavor.",
    
    "S001": "Chocolate Chip Cookie\nA freshly baked cookie packed with gooey chocolate chips—a timeless treat.",
    
    "S002": "Fudge Brownie\nDense, rich, and chocolatey with a soft interior and a crackly top—perfect with coffee.",
    
    "S003": "Classic Cinnamon Roll\nSwirls of cinnamon and sugar wrapped in soft dough, topped with sweet icing. A cozy classic.",
    
    "B001": "Lord of the Rings\nA thrilling fantasy novel by J.R.R. Tolkien, featuring an epic quest through Middle-earth.",
    
    "B002": "A Brief History of Time\nStephen Hawking’s exploration of cosmology—from black holes to the Big Bang.",
    
    "B003": "Pride and Prejudice\nJane Austen’s beloved romance about love, manners, and misunderstanding in 19th-century England."
}

 