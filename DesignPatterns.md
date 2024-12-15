# Design Patterns in Pizza Restaurant
## 1. Singleton Pattern
This pattern ensures that a class has only one instance allover the app, and can't be accessed from other place.

### How I used it:
I applied the Singleton Pattern in the InventoryManager class to ensure all parts of the system access the same inventory instance. This prevents conflicts in ingredient availability and keeps the logic centralized.

## 2. Decorator Pattern

The Decorator Pattern allows adding new behavior to an object dynamically by wrapping it with additional functionality.

### How I used it:
Used it  for adding toppings to pizzas. Toppings like Cheese, Olives, and Mushrooms wrap the base pizza object, adding their own cost and description without altering the pizza's original class.

## 3. Factory Pattern
This pattern centralizes object creation logic, allowing a single point for managing how different objects are created.

### How I used it:
Implemented a `pizza_factory` function to handle the creation of margreita and pepperoni pizzas. This keeps the pizza creation logic in one place and makes it easier to add new pizza types.
---
## 4. Strategy Pattern
This pattern defines a family of interchangeable algorithms and lets the client choose which one to use at runtime.

### How I used it:
Applied it to handle payments, where different payment methods like `paypal` and `credit_card` implement the `payment` interface, letting users select their preferred method during checkout and a speciefic method is called, also the same concept with selecting the pizza options. 

---
# Overengineering
Overengineering happens when we are trying to optimize thing or devlop too much 
till the system becomes too complex by adding unnecessary features, layers, or abstractions.

### Example of Overengineering in Our System:
Instead of breaking down responsibilities, I could have created a large Pizza class to handle everything types, toppings, costs, and payments in one place as complex class.

```
python
class Pizza:
    def __init__(self, type):
        self.type = type
        self.toppings = []
        self.cost = 5.0 if type == "Margherita" else 6.0

    def add_topping(self, topping):
        if topping == "Cheese":
            self.toppings.append("Cheese")
            self.cost += 1.0

    def pay(self, method):
        if method == "PayPal":
            print(f"Paid ${self.cost:.2f} using PayPal.")
```
#### Issues:
Violates the Single Responsibility Principle by handling too much in one class.
Hard to extend as any addition for properities will need change in code, so it just increase complexity.

### Example 2
The factory made for the pizza can be divided into more discreted factories using abstract main factory
```
python 
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self) -> 'Pizza':
        pass

    @abstractmethod
    def create_topping(self) -> 'Topping':
        pass

class MargheritaFactory(PizzaFactory):
    def create_pizza(self) -> 'Pizza':
        return Margherita()

    def create_topping(self) -> 'Topping':
        return Cheese()

class PepperoniFactory(PizzaFactory):
    def create_pizza(self) -> 'Pizza':
        return Pepperoni()

    def create_topping(self) -> 'Topping':
        return Olives()
```


#### Conclusion
this overengineering may seem that we are using patterns and modualr approaches but it; just overkill for the scope and will affect the readability of code and will require more paths to same output 