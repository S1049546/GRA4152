# Task 1:
# Part 2 of task 1:
"""
In this programme I use inheritance to establish a hierarchy between an Animal and the species Dog, BigDog and Cat. 
Each subclass inherits the attributes and methods from Animal. 
Overriding is demonstrated by each subclass providing its unique implementation of the greet. So each greet call for each animal 
has different output. 
For example, Dog overrides greet to print "woof," while BigDog overrides it further to first call Dog's greet using super().greet() 
and then add its own "Wooooof," showing polymorphism where a single method call, greet(), can result in different 
behaviors depending on the type of object invoking it. 
"""

# Part 1 of task 1:
# Doscstring is in this file. So if you call print(Animal.__init__.__doc___) you would se the doc string for the constructor for instance.

class Animal:
    """
    # # Superclass for various Animals:
    #
    """

    def __init__(self, name):
        """
        # # Constructor that constructs an instance of an Animal
        # @param name the name of the animal
        #
        """
        self._name = name
    
    def greet(self):
        """
        # # As this is a generic animal class, it raises NotImplementedError to ensure that subclasses implement this method.
        # 
        """
        raise NotImplementedError()

    def getName(self):
        """
        # # Returns the name of the animal
        # @return self._name name of the animal
        #
        """
        return self._name



class Dog(Animal):
    """
    # # Subclass of the Animal class:
    #
    """
    def __init__(self, name):
        """
        # # Constructor that is necesarry to make a Dog object
        # Dog extends the Animal class
        # @param name the name of the Dog
        #
        """
        super().__init__(name)
    
    def greet(self):
        """
        # # The Dog greets by saying woof
        #
        """
        print("woof")

class BigDog(Dog):
    """
    # # Subclass of the Dog class:
    #
    """

    def __init__(self, name):
        """
        # # Constructor of the BigDog class
        # The class extends the Dog class.
        # @param name the name of the BigDog
        #
        """
        super().__init__(name)
    
    def greet(self):
        """
        # # The BigDog greets by saying woof like Dog and then Woooof after.
        # 
        """
        super().greet()
        print("Wooooof")


class Cat(Animal):
    """
    # # Subclass of Animal:
    #
    """

    def __init__(self, name):
        """
        # # Constructor for the Cat class
        # The class extends the Animal class.
        # @param name the name of the cat
        #
        """
        super().__init__(name)
    
    def greet(self):
        """
        # # The Cat greets by saying Meow
        #
        """
        print("Meow")