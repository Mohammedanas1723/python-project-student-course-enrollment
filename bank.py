class Account:
    def __init__(self,account_number,customer_name,mobile,balance):
        self.account_number=account_number
        self.customer_name=customer_name
        self.mobile=mobile
        self.balance=balance

class Transaction:
    def __init__(self,transaction_id,transaction_type,amount,):
        self.transaction_id=transaction_id
        self.transaction_type=transaction_type
        self.amount=amount

class Bank_services:
    def __init__(self):
        self.accounts={}
        self.transactions=[]
        self.account_counter=1001
        self.transactions_counter=1

    def generate_transaction_id(self):
        transaction_id =self.transactions_counter
        self.transactions_counter+=1
        return transaction_id
    def record_transaction(self,transaction_type,amount):
        tid=self.generate_transaction_id()
        transaction=Transaction(tid,transaction_type,amount)
        self.transactions.append(transaction)

    def create_account(self):
        name=input("enter your name:")
        mobile=int(input("enter mobile number:"))
        balance=float(int(input("enter balance:")))
        if balance<0:
            print("invalid balance")
            return
        account_number=self.account_counter
        self.account_counter +=1
        new_acc=Account(account_number,name,mobile,balance)
        self.accounts[account_number]=new_acc
        print("account was  created sucessfully")
        print("account_number:",account_number)


    def deposit(self):
        account_number=int(input("enter account number"))
        if account_number not in self.accounts:
            print("account not found")
            return
        amount=float(int(input("enter amount")))
        if amount <0:
            print("invalid amount")
            return
        Account=self.accounts[account_number]
        Account.balance+=amount
        self.record_transaction=("deposit",amount)
        print("deposit succesfully!")
        print("account balance:",Account.balance)

    def withdraw(self):
        account_number=int(input("enter account number"))
        if account_number not in self.accounts:
            print("account not found")
            return
        amount=float(int(input("enter amount")))
        if amount <0:
            print("invalid amount")
            return
        account=self.accounts[account_number]
        if amount>account.balance:
            print("insufficient balance")
            return
        account.balance-=amount
        self.record_transaction=("withdrawal",amount)
        print("withdrawal successfully")
        print("account balance",account.balance)

    def transfer (self):
        sender_number=int(input("eneter sender account no:"))
        if sender_number not in self.accounts:
            print("sender not found")
            return
        reciever_number=int(input("eneter receiver account no:"))
        if reciever_number not in self.accounts:
            print("receiver not found")
            return
        if  sender_number==reciever_number:
            print("cant tranfer money same number")
            return
        amount=float(input("enter transfer amount"))
        sender=self.accounts[sender_number]
        receiver=self.accounts[reciever_number]
        if amount>sender.balance:
            print("insufficient balance")
            return
        sender.balance-=amount
        receiver.balance+=amount
        self.record_transaction(F"transfer{sender_number}to{reciever_number}",amount)
        print("tranfers succesfully")

    def view_balance(self):
        account_number=int(input("enter account number"))
        if account_number in self.accounts:
           account=self.accounts[account_number]
           print("account_number:",account.account_number)
           print("customer_name:",account.customer_name)
           print("mobile:",account.mobile)
           print("balance:",account.balance)

    def display_accounts(self):
        if not  self.accounts:
            print("no  accounts in bank")
            return
        for account in self.accounts.values():
            print("account no:",account.account_number)
            print("customer_name:",account.customer_name)
            print("mobile:",account.mobile)
            print("balance:",account.balance)

    def view_transaction(self):
        if not self.transactions:
            print("not yet transactions done")
            return
        for transaction in self.transactions:
            print("trasaction id:",transaction.transaction_id)
            print("transaction type",transaction.transaction_type)
            print("transaction amount",transaction.amount)

bank = Bank_services()

while True:

    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. View All Accounts")
    print("7. View Transactions")
    print("8. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.transfer()

        
    elif choice == "5":
        bank.view_balance()

    elif choice == "6":
        bank.display_accounts()    
    elif choice=="7":
        bank.view_transaction()        
    elif choice=="8":
        print("thank you for using canara bank")
        break
    else:
        print("invalid choice")    


            







        

                        

        
    