class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.inventory:
            print("\nItem ID already exists!")
        else:
            self.inventory[item_id] = [name, quantity, price] #add values in dictionary
            print(f"\n{name} added successfully!")

    def display_inventory(self):
        if not self.inventory:
            print("\nInventory is empty.")
        else:
            print("\nID\tName\t\tQuantity\tPrice")
            print("-" * 50)

            for item_id, (name, quantity, price) in self.inventory.items():
                print(f"{item_id}\t{name}\t\t{quantity}\t\t{price:.2f}")

    def update_item(self, item_id, quantity, price):
        if item_id in self.inventory: 
            self.inventory[item_id][1] = quantity
            self.inventory[item_id][2] = price
            print(f"\n{self.inventory[item_id][0]} updated successfully!")
        else:
            print("\nItem ID not found!")

    def delete_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("\nItem deleted successfully!")
        else:
            print("\nItem ID not found!")


inventory = Inventory()

while True:
    print("\n Inventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":   
        item_id = input("\nEnter item ID: ")
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.add_item(item_id, name, quantity, price)

    elif choice == "2":  
        inventory.display_inventory()

    elif choice == "3":  
        item_id = input("\nEnter item ID to update: ")

        if item_id in inventory.inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory.update_item(item_id, quantity, price)
        else:
            print("\nItem ID not found!")

    elif choice == "4":
        item_id = input("\nEnter item ID to delete: ")
        inventory.delete_item(item_id)

    elif choice == "5":  
        print("\nExiting the Inventory Management System. Goodbye!")
        break

    else:
        print("\nInvalid choice. Try again.")
