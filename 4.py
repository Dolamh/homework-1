class BankAccount:
  def __init__(self, account_number, account_holder):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = 0.0  # Initialize balance to 0.0

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited {amount}. New balance: {self.balance}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount > 0 and self.balance >= amount:
      self.balance -= amount
      print(f"Withdrew {amount}. New balance: {self.balance}")
    else:
      print("Insufficient funds or invalid withdrawal amount.")

  def get_balance(self):
    return self.balance

  def __str__(self):
    return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(BankAccount):
  def __init__(self, account_number, account_holder, interest_rate):
    super().__init__(account_number, account_holder)
    self.interest_rate = interest_rate

  def apply_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Applied interest of {interest}. New balance: {self.balance}")

  def __str__(self):
    return super().__str__() + f"\nInterest Rate: {self.interest_rate}"

# Create a BankAccount
my_account = BankAccount("1234567890", "Dolamah Osman")

# Deposit $1000
my_account.deposit(1000)

# Withdraw $500
my_account.withdraw(500)

# Print current balance
print(my_account)  # This will use the overridden __str__ of BankAccount

# Create a SavingsAccount instance
savings_account = SavingsAccount("9876543210", "Ali ALi", 0.05)

# Apply interest
savings_account.apply_interest()

# Print account details with interest rate
print(savings_account)
