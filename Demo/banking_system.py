from flask import Flask, render_template, request, jsonify
from banking_system import BankAccount

app = Flask(__name__)

# Create a sample account (in a real application, this would be stored in a database)
account = BankAccount("123456789", "John Doe", 1000.00)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/balance')
def get_balance():
    return jsonify({"balance": account.balance})

@app.route('/deposit', methods=['POST'])
def deposit():
    try:
        amount = float(request.json.get('amount', 0))
        result = account.deposit(amount)
        return jsonify({
            "message": result,
            "balance": account.balance,
            "transactions": account.transaction_history
        })
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

@app.route('/withdraw', methods=['POST'])
def withdraw():
    try:
        amount = float(request.json.get('amount', 0))
        result = account.withdraw(amount)
        return jsonify({
            "message": result,
            "balance": account.balance,
            "transactions": account.transaction_history
        })
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

@app.route('/transactions')
def get_transactions():
    return jsonify({"transactions": account.transaction_history})

if __name__ == '__main__':
    app.run(debug=True)