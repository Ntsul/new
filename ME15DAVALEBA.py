#####################
##15davaleba
##############################

class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan})"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell(self, buyer, loan_amount=0):
        if loan_amount == 0:
            buyer.deposit -= self.price
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
            print(f"House {self.ID} sold to {buyer.name} for {self.price}. Status: {self.status}")
        else:
            buyer.deposit -= (self.price - loan_amount)
            buyer.loan += loan_amount
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold on loan"
            print(f"House {self.ID} sold to {buyer.name} for {self.price} with a loan of {loan_amount}. Status: {self.status}")

    def __str__(self):
        return f"House(ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name}, Status: {self.status})"


seller = Person(name="Elene")
buyer = Person(name="Giorgi")

print(seller)
print(buyer)

house = House(ID="12345", price=5000, owner=seller)
print(house)

house.sell(buyer)

print(seller)
print(buyer)
print(house)

house.sell(buyer, loan_amount=2000)

print(seller)
print(buyer)
print(house)
