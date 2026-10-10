# Inventory Management System

# ADD = 0
# REMOVE = 1

# MIN_STOCK_LEVEL = 5
# MAX_QUANTITY = 1000000
# MAX_PRICE = 10000000

# VALID_UNITS = ["kg", "g", "L", "ml", "pcs"]


products = {
    101 : {
        "name" : "rice",
        "catagory" : "grains",
        "price" : 60,
        "quantity": 50,
        "unit": "kg"
    },
    102 : {
        "name" : "wheat",
        "catagory" : "grains",
        "price" : 45,
        "quantity": 40,
        "unit": "kg"       
    },
    103 : {
        "name" : "sunflower oil",
        "catagory" : "oil",
        "price" : 180,
        "quantity": 100,
        "unit": "L"
    },
    104 : {
        "name" : "jeera",
        "catagory" : "spices",
        "price" : 30,
        "quantity": 6000,
        "unit": "g"
    }
}

def add_stock(id,name,cat,price,qyt,unit):
    if id in products:
        print("The item already exists")
        try:
            check = input("Do you want to update the product? y/n: ")
            if check.lower() == "y":
                update_stock(id,price,qyt,unit)
            elif check.lower() == "n":
                print("Redirecting to the menu")
            else: 
                print("Enter a valid input")
        
        except ValueError:
            print("Invalid input! Please enter y/n.")
    else:
        products[id] = {
            "name": name,
            "catagory":cat,
            "price":price,
            "quantity":qyt,
            "unit":unit
        }
        print("The item is added successfully")

def view_items(sort_by="id"):
    if not products:
         print("No products available.")
    else:
        print("="*80)
        print(f"{'Product ID':<15}{'Name':<15}{'Catagory':<20}{'Price':<10}{'Quantity':<10}{'Unit':<10}")
        print("="*80)

        if sort_by == "id":
             sorted_products = sorted(products.items())

        elif sort_by == "name":
            sorted_products = sorted(products.items(), key=lambda x: x[1]["name"].lower())

        elif sort_by == "catagory":
            sorted_products = sorted(products.items(), key=lambda x: x[1]["catagory"].lower())

        elif sort_by == "price":
            sorted_products = sorted(products.items(), key=lambda x: x[1]["price"])

        elif sort_by == "quantity":
            sorted_products = sorted(products.items(), key=lambda x: x[1]["quantity"])

        elif sort_by == "unit":
            sorted_products = sorted(products.items(), key=lambda x: x[1]["unit"].lower())

        else:
            sorted_products = sorted(products.items())


        for product_id,prd in sorted_products:
            print(
                f"{product_id:<15}"
                f"{prd['name']:<15}"
                f"{prd['catagory']:<20}"
                f"{prd['price']:<10}"
                f"{prd['quantity']:<10}"
                f"{prd['unit']:<10}"
            )

def search_product(id):
    if id in products:
       print("="*70)
       print("Product Id.        : ", id)
       print("Product Name       : ", products[id]["name"])
       print("Product Catagory   : ", products[id]["catagory"])
       print("Product Price      : ", products[id]["price"])
       print("Product Quantity   : ", products[id]["quantity"])
       print("Product Unit       : ", products[id]["unit"])
       print("="*70)
    else:
        print("product not found.")

def update_stock(id,price,qyt,unit):
    if id in products:
       products[id]["price"] = price
       products[id]["quantity"] = qyt
       products[id]["unit"] = unit
       print("The product updated successfully")
       search_product(id)
    else:
        print("product not found.")

def updated_quantity(id,process,value):
    if id in products:
       if process == 0:
            products[id]["quantity"] += value
            print("The stock has been added successfully")
       elif process == 1:
            if products[id]["quantity"] >= value:
              products[id]["quantity"] -= value
              print("The stock has been removed successfully")
            else:
              print("Insufficent Stock")
       search_product(id)
    else:
        print("product not found.")

def delete_product(id,reid,name):
    if id in products:
        if id == reid and products[id]["name"] == name:
            del products[id]
            print("The product has been removed successfully")
            view_items()
        else:
            print("The credentials are invalid!")
    else:
         print("product not found.")

def check_stock():
    if products:
        for i in products:
           if products[i]["quantity"] <= 5:
               print("For product id", i , "the stock is below 5, please update the stock" )


def main_menu():
    print("\n========= MENU =========")
    print("1. Add Products")
    print("2. View All Products")
    print("3. Search for Product")
    print("4. Update Stock")
    print("5. Update Quantity")
    print("6. Delete product")
    print("7. Exit")

    try:
        menu_selected = int(input("Select the index from the menu: "))
        return menu_selected

    except ValueError:
        print("Invalid input! Please enter only numbers.")

while True:
    check_stock()
    menu_selected = main_menu()

    if menu_selected == 1:
        try:
            prd_id = int(input("Enter the new product id: "))
            prd_name = input("Enter the product name: ")
            prd_catagory = input("Enter the product catagory: ")
            prd_price = int(input("Enter the product price: "))
            prd_qyt = int(input("Enter the product quantity: "))
            prd_unit = input("Enter the product unit: ")
            if prd_qyt < 0 :
                print("The quantity cannot be negetive")
            elif prd_price <= 0:
                print("Invalid Price")
            else:
                add_stock(prd_id,prd_name,prd_catagory,prd_price,prd_qyt,prd_unit)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")
        

    elif menu_selected == 2:
        print("\nSort By")
        print("1. Product ID")
        print("2. Name")
        print("3. Catagory")
        print("4. Price")
        print("5. Quantity")
        print("6. Unit")

        try: 
            choice = int(input("Enter your choice: "))

            if choice == 1:
                view_items("id")

            elif choice == 2:
                view_items("name")

            elif choice == 3:
                view_items("catagory")

            elif choice == 4:
                view_items("price")

            elif choice == 5:
                view_items("quantity")

            elif choice == 6:
                view_items("unit")

        except ValueError:
            print("Invalid input! Please enter only numbers.")
    
    elif menu_selected == 3:
        try:
            id = int(input("Enter the product id: "))
            search_product(id)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")
       
    elif menu_selected == 4:
        print("Enter the Values to update the stock completely")
        try:
            prd_id = int(input("Enter the product id: "))
            prd_price = int(input("Enter the updated price: "))
            prd_qyt = int(input("Enter the updated quantity: "))
            prd_unit = input("Enter the updated unit: ")
            if prd_qyt < 0 :
                print("The quantity cannot be negetive")
            elif prd_price <= 0:
                print("Invalid Price")
            else:
                update_stock(prd_id,prd_price,prd_qyt,prd_unit)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")

    elif menu_selected == 5:
        try:
            prd_id = int(input("Enter the product id: "))
            prd_process = int(input("Enter 0 to add and 1 to remove the stock: "))
            prd_qyt = int(input("Enter the quantity to be added or removed: "))
 
            if prd_qyt < 0 :
                print("The quantity cannot be negetive")
            else:
                updated_quantity(prd_id,prd_process,prd_qyt)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")

    elif menu_selected == 6:
        try:
            prd_id = int(input("Enter the product id: "))
            reid = int(input("Contirm the product id: "))
            name = input("Enter the Name of the product: ")
 
            delete_product(prd_id,reid,name)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")

    elif menu_selected == 7:
        print("Thank you for using our Inventory Management Application.")
        break

    else:
         print("Invalid Choice! Please try again.")