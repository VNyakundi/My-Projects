# I am using flask to create this system
# the system functionality has different abilities as illustrated in the code below
# for instance, credit notes, estimates, reports and many more
# I have used CSS for styling, Javascript to make the website look more interactive.......



from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory databases (replace with real DB in production)
inventory = []
sales = []
invoices = []
time_logs = []
estimates = []
credit_notes = []
rewards = {"John Doe": 100, "Jane Smith": 150}
services = [{"name": "Repair", "price": 50}, {"name": "Installation", "price": 75}]


@app.route("/")
def dashboard():
    total_items = len(inventory)
    total_sales = len(sales)
    total_revenue = sum(sale[2] for sale in sales)
    return render_template("dashboard.html", items=total_items, sales=total_sales, revenue=total_revenue)


@app.route("/inventory", methods=["GET", "POST"])
def inventory_page():
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        inventory.append({"name": name, "price": price, "quantity": quantity})
        flash(f"Item '{name}' added successfully!", "success")
        return redirect(url_for("inventory_page"))
    return render_template("index.html", items=inventory)


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        sales.append((name, quantity, quantity * 10))  # Example price
        flash(f"Order for {quantity}x {name} placed successfully!", "success")
        return redirect(url_for("orders"))
    return render_template("orders.html", sales=sales)


@app.route("/invoices")
def invoices_page():
    return render_template("invoices.html", invoices=invoices)


@app.route("/reports")
def reports_page():
    total_revenue = sum(sale[2] for sale in sales)
    return render_template("reports.html", sales=sales, revenue=total_revenue)


@app.route("/time_logs", methods=["GET", "POST"])
def time_logs_page():
    if request.method == "POST":
        employee = request.form["employee"]
        hours = float(request.form["hours"])
        time_logs.append({"employee": employee, "hours": hours})
        flash(f"Time logged for {employee}!", "success")
        return redirect(url_for("time_logs_page"))
    return render_template("time_logs.html", logs=time_logs)


@app.route("/estimates", methods=["GET", "POST"])
def estimates_page():
    if request.method == "POST":
        items = request.form["items"]
        estimate = len(items) * 20  # Example calculation
        estimates.append({"items": items, "estimate": estimate})
        flash(f"Estimate for {items} created!", "success")
        return redirect(url_for("estimates_page"))
    return render_template("estimates.html", estimates=estimates)


@app.route("/credit_notes", methods=["GET", "POST"])
def credit_notes_page():
    if request.method == "POST":
        reason = request.form["reason"]
        amount = float(request.form["amount"])
        credit_notes.append({"reason": reason, "amount": amount})
        flash(f"Credit note for ${amount} added!", "success")
        return redirect(url_for("credit_notes_page"))
    return render_template("credit_notes.html", credit_notes=credit_notes)


@app.route("/rewards")
def rewards_page():
    return render_template("rewards.html", rewards=rewards)


@app.route("/services")
def services_page():
    return render_template("services.html", services=services)


if __name__ == "__main__":
    app.run(debug=True)
