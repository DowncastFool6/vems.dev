if __name__=="__main__":

    #Importing dictionary 
    from dictionary import electronic_stock

    #This fuction will show the electronic stock
    def show_stock():
        print("\n======== Current Inventory ========")
        for category in electronic_stock:
            print(f"\nCategory: {category}")

            for product in electronic_stock[category]["models"]:
                print(f"Product: {product['name']}")
                print(f"Quantity: {product['quantity']}")
                print("")
    
    #This function will search for a product
    def search_product():
        name = input("Type the product name: ")
        found = False

        for category in electronic_stock:
            for product in electronic_stock[category]["models"]:
                if product["name"].lower() == name.lower():
                    print("Product Found: ")
                    print(f"Name: {product['name']}")
                    print(f"Price: {product['price']}")
                    print(f"Quantity: {product['quantity']}")
                    found = True
                    return
        
        if not found:
            print("Product not found.")

    #This function is to update the price and quantity of stock
    def update_quantity():
        name = input("Type the product name: ")

        try:
            value = int(input("Indicate the quantity to add or remove: "))
        except ValueError:
            print("Invalid quantity. Please enter a postive or negative number.")
            return
        
        found = False

        for category in electronic_stock:
            for product in electronic_stock[category]["models"]:
                if product["name"].lower() == name.lower():
                    if product["quantity"] + value < 0:
                        print("Error: Insufficient stock.") 
                    else:
                        product["quantity"] += value
                        print("Quantity updated successfully!")
                        print(f"New Quantity: {product['quantity']}")
                    found = True
                    return
        
        if not found:
            print("Product not found.")

    option = 0
    while option != 4:
        print("\nSelect on of the following numbers: ")
        print("1. Show stock")
        print("2. Search for a product")
        print("3. Update product quantity")
        print("4. Exit")

        #Verifying option chosen by the user (using match and case):
        """match option:
            case 1:
                show_stock()
            case 2:
                search_product()
            case 3:
                update_quantity()
            case 4:
                print("Program Terminated")
            case _:
                print("Invalid option, please try again.")"""
        
        #Verifying option chosen by the user (using if, else):
        if option == 1:
            show_stock()
        elif option == 2:
            search_product()
        elif option == 3:
            update_quantity()
        elif option == 4:
            print("Program Terminated")
        else:
            print("Invalid option, please try again.")