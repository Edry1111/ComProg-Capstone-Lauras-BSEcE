class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (f"ID: {self.product_id}, Name: {self.name}, "
                f"Description: {self.product_description}, Price: ${self.price:.2f}, "
                f"Quantity: {self.quantity}")


def add_product(products):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        product_description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        product = Product(product_id, name, product_description, price, quantity)
        products.append(product)
        print("Product added successfully!")

def update_stock(products):
        product_id = input("Enter product ID to update: ")
        for product in products:
            if product.product_id == product_id:
                new_quantity = int(input("Enter new stock quantity: "))
                product.quantity = new_quantity
                print("Stock updated successfully!")
                return
        print("Product not found.")

def display_products(products):
        if not products:
            print("No products in inventory.")
        else:
            print("Product List:")
            for product in products:
                print(product)

def calculate_total_value(products):
        total_value = sum(product.price * product.quantity for product in products)
        print(f"Total inventory value: ${total_value:.2f}")

def main():
        courses = []
        while True:
            print("\nInventory Management Menu")
            print("1. Add Product")
            print("2. Update Stock")
            print("3. Display Products")
            print("4. Calculate Total Inventory Value")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_product(courses)
            elif choice == "2":
                update_stock(courses)
            elif choice == "3":
                display_products(courses)
            elif choice == "4":
                calculate_total_value(courses)
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
     main()
     
