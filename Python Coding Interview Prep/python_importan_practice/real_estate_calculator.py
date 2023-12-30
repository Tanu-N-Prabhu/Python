# this is real estate calculator class
class Calculator():
    total_revenue = 0.0
    # for bonus calculation
    buy = 0
    rent = 0
    pricing_rules = {}

    # get the normla pricing rules
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules

    # calculate addition
    def add(self, c):
        price = self.switch(c)
        self.total_revenue += price
        self.rules()

    # calculate bonus rules
    def rules(self):
        if self.buy > self.pricing_rules['B']['no']:
            self.total_revenue += self.pricing_rules['B']['bonus']
            self.buy -= 6
        elif self.rent > self.pricing_rules['R']['no']:
            self.total_revenue += (self.total_revenue *
                                   (self.pricing_rules['B']['bonus'] / 100))
            self.rent -= 9

    # switch case for lead codes
    def switch(self, lead_code):
        switcher = {
            'B': 10,
            'R': 5,
            'ST': 2.5
        }
        code = switcher.get(lead_code.upper(), "invalid lead code")
        if lead_code == 'b':
            self.buy += 1
        elif lead_code == 'r':
            self.rent += 1

        return code

    # return total
    def total(self):
        return self.total_revenue


pricing_rules = {'B': {'no': 5, 'bonus': 10}, 'R': {'no': 8, 'bonus': 10}}
# calculator obj
calculator = Calculator(pricing_rules)
codes = ['b', 'r', 'st']

# taking inputs until enter wrong or no code character
while True:
    lead_code = input(
        "Enter lead code [b/r/st] or any other character to break the loop: ")
    if any(lead_code in code for code in codes):
        calculator.add(lead_code)
    else:
        break

total = calculator.total()

print(f"£{total}")
