Inheritance in Python:
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. The class that inherits is called the derived or child class, and the class being inherited from is called the base or parent class.

Types of Inheritance:
1. Single Inheritance:
   - A child class inherits from a single parent class.
   - Example:
     ```python
     class Parent:
         def __init__(self, name):
             self.name = name

         def display(self):
             print(f"Parent Name: {self.name}")

     class Child(Parent):
         def __init__(self, name, age):
             super().__init__(name)
             self.age = age

         def display(self):
             super().display()
             print(f"Child Age: {self.age}")

     child = Child("John", 12)
     child.display()
     ```

2. Multiple Inheritance:
   - A child class inherits from more than one parent class.
   - Example:
     ```python
     class Parent1:
         def __init__(self, name):
             self.name = name

         def display_name(self):
             print(f"Parent1 Name: {self.name}")

     class Parent2:
         def __init__(self, age):
             self.age = age

         def display_age(self):
             print(f"Parent2 Age: {self.age}")

     class Child(Parent1, Parent2):
         def __init__(self, name, age):
             Parent1.__init__(self, name)
             Parent2.__init__(self, age)

         def display(self):
             self.display_name()
             self.display_age()

     child = Child("John", 12)
     child.display()
     ```

