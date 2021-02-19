"""Types of Methods

 -Regular
 -Class method
 -Static method

 """


class Company:
    year_raise_amount = 500
    company_age = 21

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def remove(self):
        print('Removed: ', self.name)

    def raise_salary(self):
        print('Salary raised 7k for this employee:', self.name, ', New salary: ',
              (int(self.salary) + Company.year_raise_amount))

    @classmethod
    def welcome(cls):
        print('Hey bro,this is a class method,and you can call by class name')


"""
**CLASS**
In technical terms we can say that class is a blue print for individual objects with exact behaviour.

**OBJECT**
object is one of instances of the class. which can perform the functionalities which are defined in the class.

**__init__ method**
"__init__" is a reserved method in python classes. It is called as a constructor in object oriented terminology.
This method is called when an object is created
from a class and it allows the class to initialize the attributes of the class.
It is run as soon as an object of a class is instantiated



**cls***
cls represents the instance of the class
The word 'cls' is used to represent the instance of a class. By using the "cls" keyword we access
the attributes and methods of the class in python.It binds the attributes with the given arguments.

**Class variables**

-Class variables shared among all instances of class. Class variables should be same for for each instance.

-Instance variables is unique for each instance



**TYPES OF METHODS**
-To define a class method in python, we use @classmethod decorator.
A class method can be called by class directly or by an instance

-no need to instantiate an instance to call the class method
-But a instance method can only be called by an instance.
An instance method’s first parameter is the instance who calls it.
-Regular functions belong to objects and instances. You can call regular methods with instances


*Static Method*
- It does not matter whether we call a static method by class or instance.

Why Use Static Method ?
Because static methods don’t contain parameters about a specific class or instances.
We can totally define it as an independent function out of a class and use it as other normal functions out of classes.

Define a function as a static method within a class if this function’s logic is closely related to the class.

"""
