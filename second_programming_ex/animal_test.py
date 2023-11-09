from animal import Animal
from animal import Dog
from animal import BigDog
from animal import Cat

import argparse
import textwrap

def animal_test():
    parser = argparse.ArgumentParser(prog = "Animal test program", 
                                    formatter_class = argparse.RawDescriptionHelpFormatter, 
                                    description = textwrap.dedent('''\
                                                Animal
                                    --------------------------------
                                    A program that creates animals and greets for each animal
                                    
                                    Methods:
                                    1) getName:
                                    @return name the name of the Animal
                                    
                                    2) greet:
                                    Each type of animal has its own way of greeting.
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                    --------------------------------
                                    # Initializes objects of different animals
                                    e = Animal("Esteban")           
                                    b = Dog("Bence")
                                    k = BigDog("Karl")
                                    c = Cat("Cleo")

                                    print(e.getName())
                                    print("Expected: Esteban")

                                    b.greet()
                                    print("Expected: Woof")

                                    k.greet()
                                    print("Expected Woof\nWoooof")

                                    c.greet()
                                    print("Expected: Meow")

                                    '''))
    parser.add_argument('--run_test', action='store_true', help='runs Animal test')

    args = parser.parse_args()

    if args.run_test:
        e = Animal("Esteban")
        b = Dog("Bence")
        k = BigDog("Karl")
        c = Cat("Cleo")
        print(e.getName())
        print("Expected: Esteban")

        b.greet()
        print("Expected: Woof")

        k.greet()
        print("Expected Woof\nWoooof")

        c.greet()
        print("Expected: Meow")
animal_test()





