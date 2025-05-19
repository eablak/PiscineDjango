class HotBeverage:
    
    def __init__(self, name="hot beverage", price = 0.30):
        self.name = name
        self.price = price

    def description(self):
        return f"Just some hot water in a cup."
    
    def __str__(self):
        return f"name : {self.name}\nprice :{self.price:.2f}\ndescription : {self.description()}"
    
    
class Coffe(HotBeverage):

    def __init__(self):
        super().__init__("coffee", 0.40)

    def description(self):
        return f"A coffee, to stay awake."


class Tea(HotBeverage):

    def __init__(self):
        super().__init__("tea", 0.30)

    def description(self):
        return f"Just some hot water in a cup."


class Chocolate(HotBeverage):
    
    def __init__(self):
        super().__init__("chocolate", 0.50)

    def description(self):
        return f"Chocolate, sweet chocolate..."
    

class Cappuccino(HotBeverage):

    def __init__(self):
        super().__init__("cappuccino", 0.45)

    def description(self):
        return f"Un po’ di Italia nella sua tazza!"