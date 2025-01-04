# Base class: account

class account:
    def __init__(self,account_number,account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = 0.0

    def deposit(self,amount):
        """Deposit Money into the account"""
        if amount>0:
            self._balance += amount
            print(f"${amount} deposited into account{self.account_number}.current balance:${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        """Withdraw money from the account.To be overridden in subclass"""
        raise NotImplementedError("Withdraw method must be implimented in subclass")
    
    def check_balance(self):
        """Check account balance"""
        return self._balance
    
# Subclass: Savings Account

class SavingsAccount(account):
    def __init__(self,account_number,account_holder):
        super().__init__(account_number,account_holder)
        self.interest_rate = 0.02

    def withdraw(self, amount):
        """Withdraw money with a limit check"""
        if amount>0 and amount<=self._balance:
            self._balance -= amount
            print(f"${amount}withdrawn from savings account{self.account_number}.current balance: ${self._balance}")
        else:
            print("insufficient balance or invalid withdrawal amount")

    def apply_interest(self):
        """Apply anual interest to the account balance"""
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"interest of{interest}applied.current balance: ${self._balance}")

class CheckingAccount(account):
    def __init__(self, account_number, account_holder,overdraft_limit):
        super().__init__(account_number,account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraaw money with overdraft check"""
        if amount > 0 and self._balance - amount >= self.overdraft_limit:
            self._balance -= amount
            print(f"${amount}withdrawn from checking account{self.account_number}.current balance: ${self._balance}") 
        else:
            print("insufficient balance or overdraft limit exceeded")

if __name__ == "__main__":
    #create accounts
    savings = SavingsAccount("SA123","Alice")
    checking = CheckingAccount("CA456","Bob",overdraft_limit=500)
    # Deposit money
    savings.deposit(1000)
    checking.deposit(500)
    # Withdraw money
    savings.withdraw(200)
    checking.withdraw(700)
    # Apply interest to savings account
    savings.apply_interest()
    # Check balances

    print(f"savings account balance: {savings.check_balance()}")
    print(f"checking account balance : {checking.check_balance()}")
    

        
        