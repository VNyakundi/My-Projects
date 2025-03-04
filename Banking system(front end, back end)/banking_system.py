from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

class BankAccount:
    def __init__(self, account_number, account_holder, pin, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.pin = int(pin)  # Store PIN as integer
        print(f"Account created with PIN: {self.pin}")  # Debug log
        self.balance = initial_balance
        self.transaction_history = []

    def verify_pin(self, pin):
        try:
            input_pin = int(pin)  # Convert input PIN to integer
            print(f"Verifying PIN - Input: {input_pin}, Stored: {self.pin}")  # Debug log
            return input_pin == self.pin
        except (ValueError, TypeError):
            print(f"Invalid PIN format: {pin}")  # Debug log
            return False

    def deposit(self, amount, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        if amount > 0:
            self.balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transaction_history.append({
                "type": "Deposit",
                "amount": amount,
                "timestamp": timestamp,
                "balance": self.balance
            })
            return f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.transaction_history.append({
                    "type": "Withdrawal",
                    "amount": amount,
                    "timestamp": timestamp,
                    "balance": self.balance
                })
                return f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            return "Insufficient funds."
        return "Invalid withdrawal amount. Please enter a positive number."

    def get_balance(self, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        return f"Current balance: ${self.balance:.2f}"

    def get_transaction_history(self, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        return self.transaction_history

    def generate_receipt(self, transaction):
        receipt = f"""
        ====== TRANSACTION RECEIPT ======
        Date: {transaction['timestamp']}
        Type: {transaction['type']}
        Amount: ${transaction['amount']:.2f}
        Balance: ${transaction['balance']:.2f}
        Account: {self.account_number}
        Holder: {self.account_holder}
        ================================
        """
        return receipt

# Create a sample account (in a real application, this would be stored in a database)
account = BankAccount("123456789", "Vincent Nyakundi", "0000", 1000.00)

@app.route('/')
def home():
    return render_template('index.html', account_holder=account.account_holder)

@app.route('/verify-pin', methods=['POST'])
def verify_pin():
    try:
        data = request.get_json()
        print(f"Received request data: {data}")  # Debug log
        
        if not data or 'pin' not in data:
            print("No PIN provided in request")  # Debug log
            return jsonify({"valid": False, "message": "No PIN provided"}), 400
        
        pin = str(data['pin'])  # Convert PIN to string
        print(f"Processing PIN verification for: '{pin}'")  # Debug log
        
        if account.verify_pin(pin):
            print("PIN verification successful")  # Debug log
            return jsonify({"valid": True, "message": "PIN verified successfully"})
        
        print("PIN verification failed")  # Debug log
        return jsonify({"valid": False, "message": "Invalid PIN"}), 401
        
    except Exception as e:
        print(f"Error in verify_pin route: {str(e)}")  # Debug log
        return jsonify({"valid": False, "message": "Error verifying PIN"}), 500

@app.route('/balance')
def get_balance():
    try:
        pin = request.args.get('pin')
        result = account.get_balance(pin)
        if result == "Invalid PIN":
            return jsonify({"error": result}), 401
        return jsonify({"balance": account.balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/deposit', methods=['POST'])
def deposit():
    try:
        amount = float(request.json.get('amount', 0))
        pin = request.json.get('pin')
        result = account.deposit(amount, pin)
        if result == "Invalid PIN":
            return jsonify({"error": result}), 401
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
        pin = request.json.get('pin')
        result = account.withdraw(amount, pin)
        if result == "Invalid PIN":
            return jsonify({"error": result}), 401
        return jsonify({
            "message": result,
            "balance": account.balance,
            "transactions": account.transaction_history
        })
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

@app.route('/transactions')
def get_transactions():
    try:
        pin = request.args.get('pin')
        result = account.get_transaction_history(pin)
        if result == "Invalid PIN":
            return jsonify({"error": result}), 401
        return jsonify({"transactions": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/receipt', methods=['POST'])
def get_receipt():
    try:
        pin = request.json.get('pin')
        transaction_index = request.json.get('transaction_index')
        if not account.verify_pin(pin):
            return jsonify({"error": "Invalid PIN"}), 401
        if 0 <= transaction_index < len(account.transaction_history):
            receipt = account.generate_receipt(account.transaction_history[transaction_index])
            return jsonify({"receipt": receipt})
        return jsonify({"error": "Invalid transaction index"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)