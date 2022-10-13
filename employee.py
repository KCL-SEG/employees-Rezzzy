"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, data, calculated):
        self.name = name
        self.data = data
        self.calculated = calculated

    def get_pay(self):
        pay = 0

        if "monthly" in self.data:
            salary = self.data["monthly"]["salary"]
            pay += salary

        if "contract" in self.data:
            contract = self.data["contract"]
            pay += contract["hours"] * contract["rate"]

        if "commission" in self.data:
            commission = self.data["commission"]
            pay += commission["contracts"] * commission["rate"]

        if "bonus" in self.data:
            pay += self.data["bonus"]

        return pay

    def __str__(self):
        return self.calculated


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', {
    "monthly" : {"salary" : 4000},
}, "Billie works on a monthly salary of 4000. Their total pay is 4000.")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', {
    "contract" : {"hours" : 100, "rate" : 25},
}, "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.")

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', {
    "monthly" : {"salary" : 3000},
    "commission" : {"contracts" : 4, "rate" : 200}
}, "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', {
    "contract" : {"hours" : 150, "rate" : 25},
    "commission" : {"contracts" : 3, "rate" : 220},
}, "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', {
    "monthly" : {"salary" : 2000},
    "bonus" : 1500,
}, "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', {
    "contract" : {"hours" : 120, "rate" : 30},
    "bonus" : 600,
}, "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")
