# Design Patterns 

## 1. Singleton Pattern
### What is the Singleton Pattern?  
This pattern is that each class has only one instance allover the app, can't be accessed expept from it

### How We Used It:  
We applied the Singleton Pattern in the `InventoryManager` class to ensure all parts of the system access the same inventory instance. This prevents conflicts in ingredient availability and keeps the logic centralized.

---

## 2. Decorator Pattern
### What is the Decorator Pattern?  
The Decorator Pattern allows adding new behavior to an object dynamically by wrapping it with additional functionality.

### How We Used It:  
We used the Decorator Pattern for adding toppings to pizzas. Toppings like `Cheese`, `Olives`, and `Mushrooms` wrap the base pizza object, adding their own cost and description without altering the pizza's original class.

---

## 3. Factory Pattern
### What is the Factory Pattern?  
This pattern centralizes object creation logic, allowing a single point for managing how different objects are created.

### How We Used It:  
We implemented a `pizza_factory` function to handle the creation of `Margherita` and `Pepperoni` pizzas. This keeps the pizza creation logic in one place and makes it easier to add new pizza types.

---

## 4. Strategy Pattern
### What is the Strategy Pattern?  
This pattern defines a family of interchangeable algorithms and lets the client choose which one to use at runtime.

### How We Used It:  
We applied the Strategy Pattern to handle payments. Different payment methods like `PayPalPayment` and `CreditCardPayment` implement the `PaymentStrategy` interface, letting users select their preferred method during checkout.

---

## Overengineering
### What Is Overengineering?  
Overengineering happens when a system becomes too complex by adding unnecessary features, layers, or abstractions.

### Example of Overengineering in Our System:  
Instead of breaking down responsibilities, we could have created a large `Pizza` class to handle everything—types, toppings, costs, and payments. This would have made the system harder to maintain and extend.

```python
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

### Why This Is Bad:
- Violates the **Single Responsibility Principle** by handling too much in one class.
- Hard to extend (e.g., adding a new topping or payment method requires modifying this class directly).
- Increases complexity and reduces clarity.

### How We Avoided It:  
By breaking the responsibilities into multiple classes (e.g., `Pizza`, `Topping`, `PaymentStrategy`) and applying design patterns, we kept the system clean and flexible.

