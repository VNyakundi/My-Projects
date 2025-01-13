# Enhanced Version of the Hardware store System
# Users are able to search, input to make orders
# We are also able to Add specific system rights to Admin and other members of staff....



import tkinter as tk
from tkinter import ttk, messagebox


class Item:
    """Represents an item in the inventory."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """Update the quantity of the item."""
        self.quantity += amount


class Inventory:
    """Manages the inventory of items."""
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        """Add or update an item in the inventory."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = Item(name, price, quantity)

    def search_item(self, name):
        """Search for an item in the inventory."""
        return self.items.get(name, None)

    def get_all_items(self):
        """Retrieve all items in the inventory."""
        return self.items.values()


class SalesManager:
    """Manages all sales transactions."""
    def __init__(self, inventory):
        self.inventory = inventory
        self.sales = []
        self.total_revenue = 0

    def make_sale(self, item_name, quantity):
        """Process a sale."""
        item = self.inventory.items.get(item_name)
        if item and item.quantity >= quantity:
            total_price = item.price * quantity
            self.sales.append((item_name, quantity, total_price))
            self.total_revenue += total_price
            item.update_quantity(-quantity)
            return True, total_price
        return False, 0

    def get_sales(self):
        """Retrieve all sales transactions."""
        return self.sales

    def get_revenue(self):
        """Get total revenue."""
        return self.total_revenue


class HardwareStoreApp:
    """Tkinter-based GUI for the hardware store system."""
    def __init__(self, root):
        self.root = root
        self.root.title("Hardware Store Management System")
        self.inventory = Inventory()
        self.sales_manager = SalesManager(self.inventory)

        # Frames
        self.create_frames()

        # Populate UI
        self.create_inventory_section()
        self.create_sales_section()
        self.create_admin_section()

    def create_frames(self):
        """Create layout frames."""
        self.inventory_frame = ttk.LabelFrame(self.root, text="Inventory Management", padding=10)
        self.inventory_frame.grid(row=0, column=0, padx=10, pady=10)

        self.sales_frame = ttk.LabelFrame(self.root, text="Sales Management", padding=10)
        self.sales_frame.grid(row=0, column=1, padx=10, pady=10)

        self.admin_frame = ttk.LabelFrame(self.root, text="Admin Actions", padding=10)
        self.admin_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def create_inventory_section(self):
        """Create the inventory section."""
        # Labels and Entries
        tk.Label(self.inventory_frame, text="Item Name:").grid(row=0, column=0, sticky="w", pady=2)
        self.item_name_entry = tk.Entry(self.inventory_frame)
        self.item_name_entry.grid(row=0, column=1, pady=2)

        tk.Label(self.inventory_frame, text="Price:").grid(row=1, column=0, sticky="w", pady=2)
        self.price_entry = tk.Entry(self.inventory_frame)
        self.price_entry.grid(row=1, column=1, pady=2)

        tk.Label(self.inventory_frame, text="Quantity:").grid(row=2, column=0, sticky="w", pady=2)
        self.quantity_entry = tk.Entry(self.inventory_frame)
        self.quantity_entry.grid(row=2, column=1, pady=2)

        # Add Button
        tk.Button(self.inventory_frame, text="Add/Update Item", command=self.add_item).grid(row=3, column=0, columnspan=2, pady=5)

        # Inventory Table
        self.inventory_table = ttk.Treeview(self.inventory_frame, columns=("Price", "Quantity"), show="headings")
        self.inventory_table.heading("Price", text="Price")
        self.inventory_table.heading("Quantity", text="Quantity")
        self.inventory_table.grid(row=4, column=0, columnspan=2, pady=10)

    def create_sales_section(self):
        """Create the sales section."""
        # Labels and Entries
        tk.Label(self.sales_frame, text="Item Name:").grid(row=0, column=0, sticky="w", pady=2)
        self.sale_item_entry = tk.Entry(self.sales_frame)
        self.sale_item_entry.grid(row=0, column=1, pady=2)

        tk.Label(self.sales_frame, text="Quantity:").grid(row=1, column=0, sticky="w", pady=2)
        self.sale_quantity_entry = tk.Entry(self.sales_frame)
        self.sale_quantity_entry.grid(row=1, column=1, pady=2)

        # Sale Button
        tk.Button(self.sales_frame, text="Make Sale", command=self.make_sale).grid(row=2, column=0, columnspan=2, pady=5)

        # Sales Table
        self.sales_table = ttk.Treeview(self.sales_frame, columns=("Quantity", "Total Price"), show="headings")
        self.sales_table.heading("Quantity", text="Quantity")
        self.sales_table.heading("Total Price", text="Total Price")
        self.sales_table.grid(row=3, column=0, columnspan=2, pady=10)

    def create_admin_section(self):
        """Create admin section."""
        tk.Button(self.admin_frame, text="View Revenue", command=self.view_revenue).grid(row=0, column=0, pady=5)

    def add_item(self):
        """Add or update an item in the inventory."""
        name = self.item_name_entry.get().strip()
        try:
            price = float(self.price_entry.get().strip())
            quantity = int(self.quantity_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Price and Quantity must be valid numbers.")
            return

        self.inventory.add_item(name, price, quantity)
        self.update_inventory_table()
        messagebox.showinfo("Success", f"{name} added/updated in inventory!")

    def update_inventory_table(self):
        """Refresh the inventory table."""
        for row in self.inventory_table.get_children():
            self.inventory_table.delete(row)

        for item in self.inventory.get_all_items():
            self.inventory_table.insert("", "end", values=(item.name, item.price, item.quantity))

    def make_sale(self):
        """Process a sale."""
        name = self.sale_item_entry.get().strip()
        try:
            quantity = int(self.sale_quantity_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a valid number.")
            return

        success, total_price = self.sales_manager.make_sale(name, quantity)
        if success:
            self.update_inventory_table()
            self.sales_table.insert("", "end", values=(quantity, total_price))
            messagebox.showinfo("Success", f"Sold {quantity} of {name} for ${total_price}!")
        else:
            messagebox.showerror("Failed", "Sale failed. Item not found or insufficient stock.")

    def view_revenue(self):
        """Show total revenue."""
        revenue = self.sales_manager.get_revenue()
        messagebox.showinfo("Total Revenue", f"Total Revenue: ${revenue}")


if __name__ == "__main__":
    root = tk.Tk()
    app = HardwareStoreApp(root)
    root.mainloop()
