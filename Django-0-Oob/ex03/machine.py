from beverages import HotBeverage, Coffe, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:

    class EmpytCup(HotBeverage):  
        def __init__(self):
            super().__init__("empty cup", 0.90)

        def description(self):
            return "An empty cup?! Gimme my money back!"
        
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    

    def __init__(self):
        self.status = 10

    def repair(self):
        self.status = 10

    def serve(self, drink: HotBeverage) -> HotBeverage: #just annotations not restricted
        if self.status <= 0:
            raise self.BrokenMachineException
        self.status -= 1
        if random.randint(0,5) == 0:
            return self.EmpytCup()
        return drink



if __name__ == "__main__":

    coffemach = CoffeeMachine()
    drinks = [HotBeverage() ,Coffe(), Tea(), Chocolate(), Cappuccino()]
       
    for i in range(12):
        try:
            rand_drink = random.choice(drinks)
            print(coffemach.serve(rand_drink))
            print("\n")
        except coffemach.BrokenMachineException as e:
            print(e)
            coffemach.repair()
            print("\n")