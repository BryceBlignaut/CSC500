
# define class
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.__balance = float(balance)
        self.owner_name = owner_name
# gets the balance
    def get_balance(self):
        return self.__balance
    
# wont process the balance increase if balance is set over 100,000
    def set_balance(self, balance):
        if balance < 100000:
            self.__balance = balance
        else:
            print("Unable to process transaction")

new_customer = BankAccount(123548,10, "Bryce")

# prints attributes a updates the new balance with a control if the balance is too high 
print(new_customer.account_number)
print(new_customer.owner_name)
print(new_customer.get_balance())

new_customer.set_balance(100001)


        
    

    
