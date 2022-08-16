from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        total_price = 0
        order_description = '******\nOrder Time: {}\n'.format(self.time)
        for order in self.pizzas:
            order_description += order.getPizzaDetails()
            order_description += '\n----\n'
            total_price += order.price
        order_description += 'TOTAL ORDER PRICE: ${:.2f}\n******\n'.format(total_price)
        return order_description
    def __gt__(self, rhs):
        if self.getTime() > rhs.getTime():
            return True
        else:
            return False
    def __lt__(self, rhs):
        if self.getTime() < rhs.getTime():
            return True
        else:
            return False


