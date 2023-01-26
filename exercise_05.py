class BankAccount:
    def __init__(person, account_name, balance):
        person.account_name = account_name
        person.bal = balance
    
    def deposit(person, amount):
        person.bal += amount #adds the amount to the person's balance
        return person.bal
    
    def withdraw(person, amount):
        person.bal -= amount #subtracts the amount from the balance
        return person.bal
    
    def get_balance(person):
        return '{} has a balance of {}'.format(person.account_name, person.bal) 
        #the format put the variables in the {} respectively per parameter

my_account = BankAccount('Jensen Lobo', 70.16) #hardcoded information, making an instance of the BankAccount Class
my_account.deposit(50)
my_account.withdraw(10.16)
print(my_account.get_balance()) 