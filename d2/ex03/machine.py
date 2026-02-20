import random
from beverages import HotBeverage

class CoffeeMachine:
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
         def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def __init__(self):
        self.working = True
        self.served_count = 0
    
    def repair(self):
        self.working = True
        self.served_count = 0

    def serve(self, beverage_class):
        if not self.working:
            raise CoffeeMachine.BrokenMachineException()

        # Rastgele olarak içecek veya boş bardak
        result = beverage_class() if random.choice([True, False]) else CoffeeMachine.EmptyCup()

        self.served_count += 1

        # Makine 10 içecekten sonra bozulur
        if self.served_count >= 10:
            self.working = False

        return result 

if __name__ == "__main__":
    from beverages import Coffee, Tea, Chocolate, Cappuccino

    machine = CoffeeMachine()
    drinks_list = [Coffee, Tea, Chocolate, Cappuccino]

    # Makineyi servis edene kadar döngü
    # while True:
    try:
        for _ in range(3):  # 3 kere dene, makine bozulacak
            drink_class = random.choice(drinks_list)
            drink = machine.serve(drink_class)
            print(drink)
            print()
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        print("Makine tamir ediliyor...")
        machine.repair()
        print("Makine tamir edildi, tekrar servis başlıyor...\n")