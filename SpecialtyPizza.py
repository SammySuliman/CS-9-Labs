from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        if self.size == 'S':
            self.price = 12.00
        elif self.size == 'M':
            self.price = 14.00
        elif self.size == 'L':
            self.price = 16.00
        self.name = name
    def getPizzaDetails(self):
        pizza_details = 'SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n'.format(self.size, self.name, self.price)
        return pizza_details
 
