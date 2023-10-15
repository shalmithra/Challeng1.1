class BankAccount:
  def __init__(self, account_holder, initial_balance=0):
      self.__account_holder = account_holder
      self.__balance = initial_balance

  def get_balance(self):
      return self.__balance

  def deposit(self, amount):
      if amount > 0:
          self.__balance += amount
          return f"${amount} deposited. New balance is ${self.__balance}"
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__balance:
          self.__balance -= amount
          return f"${amount} withdrawn. New balance is ${self.__balance}"
      else:
          return "Invalid withdrawal amount or insufficient funds."

  def get_account_holder(self):
      return self.__account_holder

  def set_account_holder(self, new_holder):
      self.__account_holder = new_holder

  def __str__(self):
      return f"Account Holder: {self.__account_holder}\nBalance: ${self.__balance}"

# Usage example:
if __name__ == "__main__":
  account = BankAccount("John Doe", 1000)
  print(account)
  print(account.deposit(500))
  print(account.withdraw(200))
  account.set_account_holder("Jane Smith")
  print(account)