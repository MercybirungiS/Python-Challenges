# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,amount):
      if amount<=0:
        return "Enter more money"
      else:
         self.balance+=amount

      return "Hello  {} you have deposited {} . Your new balance is {}".format(self.name,amount,self.balance)


    def withdraw(self,withdrawal):
        if (self.balance<withdrawal):
          return "Insufficient balance"
        else :
            self.balance-=withdrawal
        return " Hello {} , you have withdrawn {} . Your new balance is {}".format(self.name,withdrawal,self.balance)

    def bankfees(self , fees):
        self.balance= self.balance * fees
        return "Hello {} , your new balance is {}".format(self.name,self.balance )

    def display (self):
        print("Account Number :" ,self.account_number)
        print("Account Name :" ,self.name)
        print("Acount Balance :" , self.balance)


newAccount=BankAccount(233444,"Carol",5000)
print(newAccount.deposit(900))
print(newAccount.withdraw(500))
print(newAccount.bankfeees)
print(newAccount.display)




    

