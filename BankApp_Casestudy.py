class Account:
    def __init__(self, account_number, name, initial_balance):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
        else:
            print("Insufficient balance")

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            self.transactions.append(f"Transferred {amount} to {target_account.account_number}")
        else:
            print("Insufficient balance")

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

def create_account(accounts):
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder's Name: ")
    initial_balance = float(input("Enter Initial Balance: "))
    accounts[account_number] = Account(account_number, name, initial_balance)
    print(f"Account {account_number} created successfully!")

def view_account(accounts):
    account_number = input("Enter Account Number: ")
    account = accounts.get(account_number)
    if account:
        print(f"Account Number: {account.account_number}")
        print(f"Name: {account.name}")
        print(f"Balance: {account.balance}")
    else:
        print("Account not found")

def withdraw_amount(accounts):
    account_number = input("Enter Account Number: ")
    account = accounts.get(account_number)
    if account:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    else:
        print("Account not found")

def deposit_amount(accounts):
    account_number = input("Enter Account Number: ")
    account = accounts.get(account_number)
    if account:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    else:
        print("Account not found")

def transfer_funds(accounts):
    from_account_number = input("Enter Your Account Number: ")
    to_account_number = input("Enter Account Number to Transfer to: ")
    amount = float(input("Enter amount to transfer: "))
    from_account = accounts.get(from_account_number)
    to_account = accounts.get(to_account_number)
    if from_account and to_account:
        from_account.transfer(to_account, amount)
    else:
        print("One or both accounts not found")

def print_transaction(accounts):
    account_number = input("Enter Account Number: ")
    account = accounts.get(account_number)
    if account:
        account.print_transactions()
    else:
        print("Account not found")

accounts = {}
while True:
    choice = input(
    """
    1. Create Account
    2. View Account Details
    3. Withdraw
    4. Deposit
    5. Fund Transfer
    6. Print Transaction
    7. Exit 
    """)
    if choice == '1':
        create_account(accounts)
    elif choice == '2':
        view_account(accounts)
    elif choice == '3':
        withdraw_amount(accounts)
    elif choice == '4':
        deposit_amount(accounts)
    elif choice == '5':
        transfer_funds(accounts)
    elif choice == '6':
        print_transaction(accounts)
    elif choice == '7':
        break
    else:
        print("Please Enter a valid choice")
