class Account:
    def __init__(self, balance,name):
        self.balance = balance
        self.name = name

    def deposit(self,deposit):
        self.balance=self.balance + deposit
        print(self.get_name (), "deposited ", deposit)

    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        print(self.get_name(),"withdrawn ",withdraw)
        print(self.get_name (), "has a balance of ", self.get_balance())

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name=name
        print("The customer name is", name, "the balance is ",self.balance)

customer1 = Account(0,"Bandula")
customer1.deposit(10000)

customer1.withdraw(2000)
customer1.withdraw(3000)
customer1.set_name("Bandula Vedage")
customer1.withdraw(1000)

