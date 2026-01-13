if __name__=="__main__":

    product_set = {"bread", "milk", "rice", "apple"}


    print(f"======== A list of products. ======== \n{product_set}")

    while True:
        product = input('\nEnter a product to add (or type "exit" to finish):')
        product.lower()

        if product == "exit":
            break
        if product in product_set:
            print("Product already exists in the list!")

        else:
            product_set.add(product)
            print("Product added.")

    print(f"\n======== Final product list in order. ========")
    
    new_products = sorted(product_set)
    print("\n", new_products)
