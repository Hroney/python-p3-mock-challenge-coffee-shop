class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value

        
    def orders(self):
        returnArray = []

        for value in Order.all:
            if value.coffee.name == self.name:
                returnArray.append(value)
        return returnArray
    
    def customers(self):
        returnArray = []

        for value in Order.all:
            if value.coffee.name == self.name:
                if value.customer not in returnArray:
                    returnArray.append(value.customer)
        return returnArray
    
    def num_orders(self):
        num = 0
        for value in Order.all:
            if value.coffee.name == self.name:
                num += 1
        return num
    
    def average_price(self):
        num = []
        for value in Order.all:
            if value.coffee.name == self.name:
                num.append(value.price)
        return sum(num) / len(num)

class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and (len(value) >= 1 and len(value) <= 15):
            self._name = value

    def orders(self):
        returnArray = []
        for value in Order.all:
            if value.customer.name == self.name:
                returnArray.append(value)
        return returnArray
    
    def coffees(self):
        returnArray = []
        for value in Order.all:
            if value.customer.name == self.name and value.coffee not in returnArray:
                returnArray.append(value.coffee)
        return returnArray
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        self._coffee = value        
   
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) and (value >= 1.0 and value <= 10.0) and not hasattr(self, 'price'):
            self._price = value
