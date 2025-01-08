Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code in the form of procedures (often known as methods). A key feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated. In OOP, computer programs are designed by making them out of objects that interact with one another.

The four main principles of OOP are:

1. **Encapsulation**: This is the concept of wrapping the data (variables) and the code (methods) together as a single unit. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. Access to the data is typically provided through public methods. Encapsulation helps to achieve a modular structure in the code, making it easier to maintain and understand.
   - **Example**: In a class representing a bank account, the balance attribute can be private, and access to it can be provided through public methods like deposit() and withdraw().
   ```python
   class BankAccount:
       def __init__(self, initial_balance):
           self.__balance = initial_balance

       def deposit(self, amount):
           self.__balance += amount

       def withdraw(self, amount):
           if amount <= self.__balance:
               self.__balance -= amount
           else:
               print("Insufficient funds")

       def get_balance(self):
           return self.__balance

   account = BankAccount(100)
   account.deposit(50)
   print(account.get_balance())  # Output: 150
   account.withdraw(75)
   print(account.get_balance())  # Output: 75
   ```

2. **Abstraction**: This principle involves hiding the complex implementation details and showing only the necessary features of the object. It helps in reducing programming complexity and effort. Abstraction allows a programmer to focus on interactions at a higher level without needing to understand all the underlying details.
   - **Example**: When using a car, you only need to know how to drive it (interface) and not how the engine works (implementation details).
   ```python
   from abc import ABC, abstractmethod

   class Vehicle(ABC):
       @abstractmethod
       def start_engine(self):
           pass

   class Car(Vehicle):
       def start_engine(self):
           print("Engine started")

   my_car = Car()
   my_car.start_engine()  # Output: Engine started
   ```

3. **Inheritance**: This is a mechanism where a new class inherits the properties and behavior of an existing class. It provides the idea of reusability and can lead to a hierarchical classification. Inheritance allows for the creation of a new class that is a modified version of an existing class, promoting code reuse and reducing redundancy.
   - **Example**: A class `Animal` can have subclasses like `Dog` and `Cat` that inherit attributes and methods from `Animal`, but also have their own specific attributes and methods.
   ```python
   class Animal:
       def __init__(self, name):
           self.name = name

       def speak(self):
           pass

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   dog = Dog("Buddy")
   cat = Cat("Whiskers")
   print(dog.speak())  # Output: Woof!
   print(cat.speak())  # Output: Meow!
   ```

4. **Polymorphism**: This allows methods to do different things based on the object it is acting upon, even though they share the same name. It is the ability to present the same interface for different underlying forms (data types). Polymorphism enables objects of different classes to be treated as objects of a common super class, primarily through method overriding and method overloading.
   - **Example**: A method named `draw()` can be used for different shapes like circles, squares, and triangles. Each shape class can have its own implementation of the `draw()` method.
   ```python
   class Shape:
       def draw(self):
           pass

   class Circle(Shape):
       def draw(self):
           print("Drawing a circle")

   class Square(Shape):
       def draw(self):
           print("Drawing a square")

   shapes = [Circle(), Square()]
   for shape in shapes:
       shape.draw()
   # Output:
   # Drawing a circle
   # Drawing a square
   ```

In Python, the method resolution order (MRO) determines which method is called when there are multiple methods with the same name in a class hierarchy. The MRO is determined by the C3 linearization algorithm, which Python uses to create a consistent order for method resolution.
You can inspect the MRO of a class using the __mro__ attribute or the mro() method.