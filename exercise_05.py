class BankAccount:
    def __init__(person, account_name, balance):
        person.account_name = account_name
        person.bal = balance
    
    def deposit(person, amount):
        person.bal += amount
        return person.bal
    
    def withdraw(person, amount):
        person.bal -= amount
        return person.bal
    
    def get_balance(person):
        return '{} has a balance of {}'.format(person.account_name, person.bal)

my_account = BankAccount('Jensen Lobo', 70.16)
my_account.deposit(50)
my_account.withdraw(10.16)
print(my_account.get_balance())