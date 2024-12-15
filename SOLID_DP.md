# Recap for what each solid princple do

### - Single Reposnbility
Each class should have it's own functionality, not one class making many functions
### - Open-Closed
Classes have to be able to be expanded smoothly without restructuring the current code
### - liskov
having abtractability which be sufficient for being able to take subclasses with no issues, like polymerphism 
### - Interface Segregation Principle
 minimal builds and no excessive or unnecessary methods for using the class.
### - Dependency Inversion Principle
high-level classes (the "main logic") should not depend on low-level classes (specific implementations). Both should depend on abstractions
---
# My patterns

## 1. Singleton Pattern
we wanted to use the same instance of the Inventory allover the system, as the ingredients and their quantitiy is a centralized thing cant be controller from many sides, so i applied singlton in the InventoryManager class
### how this is related to SOLID princples: 
This is related to the Songle responsbility princple and Interface segregation, where the operations related to inventory will just be made by it, also the Lsp as it can't be subclassed 

## 2. Decorator
As required we wanted the system to allow customers to add toppings dynamically without needing to rewrite or modify the base pizza classes, so I applied the Decorator Pattern in the Topping classes that are responsible for adding the topping to a selected piiza, so they take the pizza object and add to it the topping object. So the dcorator acts as a wrapper to the Pizza class

### How this is related to SOLID principles:
This is related to the Open-Closed Principle because we can add new toppings without modifying existing classes. It also follows Single Responsibility since each topping is responsible for adding its cost and description to the pizza. Lastly, the Liskov Substitution Principle is applied since the Topping classes behave like Pizza objects.

## 3. Factory 
We needed to centralize the creation of pizzas to avoid messy logic for creating different pizza types, so I used a Factory function to handle pizza creation where the function take the type of pizza and redirect to return the desired pizza object from it's class, so code is centralized.

### How this is related to SOLID principles:
This is related to the Single Responsibility Principle, as the Factory function focuses only on pizza creation. It also aligns with the Open-Closed Principle since we can add new pizza types without modifying the existing logic.