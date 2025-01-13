# Hardware Management System
# I Am Using Object Oriented Programming to code and develop this system
# Framework - Django/Flask
# Front end - Css, Javascript



class Item:
    """Represents an item in the inventory."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """Update the quantity of the item."""
        self.quantity += amount

    def display_details(self):
        """Display item details."""
        print(f"Item: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")


class Inventory:
    """Manages the inventory of items."""
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        """Add a new item to the inventory."""
        if name in self.items:
            print(f"{name} already exists. Updating quantity.")
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = Item(name, price, quantity)
        print(f"Added {quantity} of {name} to inventory.")

    def remove_item(self, name):
        """Remove an item from the inventory."""
        if name in self.items:
            del self.items[name]
            print(f"Removed {name} from inventory.")
        else:
            print(f"{name} does not exist in inventory.")

    def update_stock(self, name, quantity):
        """Update the stock of an item."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
            print(f"Updated {name} stock by {quantity}.")
        else:
            print(f"{name} does not exist in inventory.")

    def view_inventory(self):
        """View all items in the inventory."""
        print("\nInventory:")
        if self.items:
            for item in self.items.values():
                item.display_details()
        else:
            print("No items in inventory.")

    def find_item(self, name):
        """Find an item by name."""
        return self.items.get(name, None)

    def view_low_stock(self, threshold=5):
        """View items that are low in stock."""
        print("\nLow Stock Items:")
        low_stock = [item for item in self.items.values() if item.quantity <= threshold]
        if low_stock:
            for item in low_stock:
                item.display_details()
        else:
            print("No low-stock items.")


class Sale:
    """Represents a single sale transaction."""
    def __init__(self, item_name, quantity, total_price):
        self.item_name = item_name
        self.quantity = quantity
        self.total_price = total_price

    def display_sale(self):
        """Display sale details."""
        print(f"Sold {self.quantity} of {self.item_name} for ${self.total_price}")


class SalesManager:
    """Manages all sales transactions."""
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = []
        self.total_revenue = 0

    def make_sale(self, item_name, quantity):
        """Record a sale."""
        item = self.inventory.find_item(item_name)
        if item and item.quantity >= quantity:
            total_price = item.price * quantity
            self.sales.append(Sale(item_name, quantity, total_price))
            self.total_revenue += total_price
            item.update_quantity(-quantity)
            print(f"Sale successful: {quantity} of {item_name} sold for ${total_price}")
        else:
            print(f"Sale failed: {item_name} is either out of stock or insufficient quantity.")

    def view_sales(self):
        """View all sales transactions."""
        print("\nSales Transactions:")
        if self.sales:
            for sale in self.sales:
                sale.display_sale()
        else:
            print("No sales recorded.")

    def view_revenue(self):
        """View total revenue."""
        print(f"\nTotal Revenue: ${self.total_revenue}")


# Testing the Hardware Store Management System
if __name__ == "__main__":
    # Create Inventory
    inventory = Inventory()

    # Create SalesManager
    sales_manager = SalesManager(inventory)

    # Add items to inventory
    inventory.add_item("Hammer", 10, 15)
    inventory.add_item("Screwdriver", 5, 10)
    inventory.add_item("Wrench", 8, 3)

    # View inventory
    inventory.view_inventory()

    # View low stock items
    inventory.view_low_stock()

    # Make sales
    print("\nMaking Sales:")
    sales_manager.make_sale("Hammer", 2)
    sales_manager.make_sale("Wrench", 4)  # Should fail due to insufficient stock
    sales_manager.make_sale("Screwdriver", 5)

    # View sales transactions
    sales_manager.view_sales()

    # View total revenue
    sales_manager.view_revenue()

    # Update stock
    inventory.update_stock("Wrench", 10)

    # View inventory after stock update
    inventory.view_inventory()




