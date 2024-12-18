from abc import ABC, abstractmethod


# Singleton Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls): # added this to make it a singleton, where only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance
    
    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

# ----------  one pizze (core) ----------
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# ---------- factory ----------
def pizza_factory(pizza_type: str) -> Pizza:
    if pizza_type == "1": # number passed in the input
        return Margherita()
    elif pizza_type == "2":
        return Pepperoni()
    
# ----------- toppings ----------
class topping(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        self._inventory_manager = InventoryManager() 

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()
    def add_topping(self):
        pass

class Cheese(topping):
    def get_description(self):
        if self._inventory_manager.check_and_decrement("Cheese"):
            return self.pizza.get_description() + ", Cheese"
        print("Cheese is out of stock!")
        return self.pizza.get_description()

    def get_cost(self):
        if self._inventory_manager.check_and_decrement("Cheese"):
            return self.pizza.get_cost() + 1.0
        return self.pizza.get_cost()

class Olives(topping):
    def get_description(self):
        if self._inventory_manager.check_and_decrement("Olives"):
            return self.pizza.get_description() + ", Olives"
        print("Olives are out of stock!")
        return self.pizza.get_description()

    def get_cost(self):
        if self._inventory_manager.check_and_decrement("Olives"):
            return self.pizza.get_cost() + 0.5
        return self.pizza.get_cost()

class Mushrooms(topping):
    def get_description(self):
        if self._inventory_manager.check_and_decrement("Mushrooms"):
            return self.pizza.get_description() + ", Mushrooms"
        print("Mushrooms are out of stock!")
        return self.pizza.get_description()

    def get_cost(self):
        if self._inventory_manager.check_and_decrement("Mushrooms"):
            return self.pizza.get_cost() + 0.7
        return self.pizza.get_cost()

      
    
# ----------- types ----------
class Margherita(Pizza):
    def get_description(self):
        return "Margherita Pizza"

    def get_cost(self):
        return 5.0

class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni Pizza"

    def get_cost(self):
        return 6.0
# --------- payment ----------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class paypal(Payment):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal")

class credit_card(Payment):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card")


# Main Function
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")


    while True:

        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        
        if pizza_choice in ["1", "2"]:
            pizza = pizza_factory(pizza_choice) # create the pizze using the factory
        elif pizza_choice == "0":
            break
        else:
            print("This Pizza is unavailable")
            continue


        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")
            # TODO: fill the following as required
            # Cheese
            if topping_choice == "1" :
                pizza = Cheese(pizza)
            # Olive
            elif topping_choice == "2":
                pizza = Olives(pizza)
            # Mushrooms
            elif topping_choice == "3":
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # --------  Payment ---------
        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")
        if payment_choice == "1":
            payment = paypal()
        elif payment_choice == "2":
            payment = credit_card()
        else:
            print("Payment method unavailable")
            continue

        payment.pay(pizza.get_cost())

        # Show final inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

        # ------------------


if __name__ == "__main__":
    main()

