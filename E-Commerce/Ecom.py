import pandas as pd

# Sample product data
product_data = {
    'Product ID': [101, 102, 103, 104, 105],
    'Product Name': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Camera'],
    'Price': [1000, 500, 100, 300, 700],
    'Stock': [10, 20, 30, 15, 5]
}

# Load product data into pandas DataFrame
product_df = pd.DataFrame(product_data)

# Function to display available products
def display_products():
    print("\nAvailable Products:")
    print(product_df)

# Function to add a new product
def add_product(product_id, product_name, price, stock):
    global product_df
    new_product = pd.DataFrame({'Product ID': [product_id], 'Product Name': [product_name], 'Price': [price], 'Stock': [stock]})
    product_df = pd.concat([product_df, new_product], ignore_index=True)
    print("\nProduct added successfully!")

# Function to remove a product
def remove_product(product_id):
    global product_df
    product_df = product_df[product_df['Product ID'] != product_id]
    print("\nProduct removed successfully!")

# Function to purchase a product
def purchase_product(product_id, quantity):
    global product_df
    product_index = product_df.index[product_df['Product ID'] == product_id].tolist()
    if product_index:
        product_index = product_index[0]
        if product_df.at[product_index, 'Stock'] >= quantity:
            product_df.at[product_index, 'Stock'] -= quantity
            print(f"\nPurchase successful! Total cost: Rs{product_df.at[product_index, 'Price'] * quantity}")
        else:
            print("\nUnfortunately, the item is currently unavailable.")
    else:
        print("\nProduct not found.")

# Main function
def main():
    while True:
        print("\n\t\t\tE-commerce Platform")
        print("\nMain menu:")
        print("1. Display Available Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Purchase Product")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_products()
        elif choice == '2':
            product_id = int(input("Enter Product ID: "))
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            add_product(product_id, product_name, price, stock)
        elif choice == '3':
            product_id = int(input("Enter Product ID to remove: "))
            remove_product(product_id)
        elif choice == '4':
            product_id = int(input("Enter Product ID to purchase: "))
            quantity = int(input("Enter Quantity: "))
            purchase_product(product_id, quantity)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
