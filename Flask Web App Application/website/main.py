from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for flashing messages

# Data Models
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


# Initialize Inventory and Sales Manager
inventory = Inventory()
sales_manager = SalesManager(inventory)

# Routes
@app.route("/")
def home():
    """Home page to display inventory."""
    items = inventory.get_all_items()
    return render_template("index.html", items=items)


@app.route("/add_item", methods=["POST"])
def add_item():
    """Add an item to the inventory."""
    name = request.form["name"]
    try:
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
    except ValueError:
        flash("Price and Quantity must be valid numbers.", "error")
        return redirect(url_for("home"))

    inventory.add_item(name, price, quantity)
    flash(f"{name} added/updated successfully!", "success")
    return redirect(url_for("home"))


@app.route("/make_sale", methods=["POST"])
def make_sale():
    """Make a sale."""
    name = request.form["sale_name"]
    try:
        quantity = int(request.form["sale_quantity"])
    except ValueError:
        flash("Quantity must be a valid number.", "error")
        return redirect(url_for("home"))

    success, total_price = sales_manager.make_sale(name, quantity)
    if success:
        flash(f"Sold {quantity} of {name} for KES{total_price:.2f}!", "success")
    else:
        flash("Sale failed. Item not found or insufficient stock.", "error")
    return redirect(url_for("home"))


@app.route("/revenue")
def view_revenue():
    """View total revenue."""
    revenue = sales_manager.get_revenue()
    return render_template("revenue.html", revenue=revenue, sales=sales_manager.get_sales())


# Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
