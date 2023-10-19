# Part of Business P9.26:
# Test program for the Customer class:
def customer_test():
    from customer import Customer
    import argparse
    import textwrap
    parser = argparse.ArgumentParser(prog = "Customer test program", 
                                    formatter_class = argparse.RawDescriptionHelpFormatter, 
                                    description = textwrap.dedent('''\
                                                Customer
                                    --------------------------------
                                    A program that simultes a customer and that tracks if the customer has a discount or not.
                                    
                                    Methods:
                                    1) makePurchase: Checks if the customer has a discount to use, and updates the value the customer has spent.
                                    @param amount the amount the customer buys for.
                                    
                                    2) discountReached:
                                    @return if a customer has a discount or not
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                    --------------------------------
                                    c1 = Customer()                 # Initializes a customer object
                                    c1.makePurchase(110)            # Makes a purchase of 110$
                                    print(c1.discountReached())     # Checkes if customer has a discount
                                    c1.makePurchase(60)             # Makes a purchase of 60$
                                    print(c1.discountReached())     # Checkes if customer has a discount
                                    c1.makePurchase(20)             # Makes a purchase of 20$
                                    print(c1.discountReached())     # Checkes if customer has a discount
                                    c1.makePurchase(90)             # Makes a purchase of 90$
                                    print(c1.discountReached())     # Checkes if customer has a discount

                                    '''))
    parser.add_argument('--run_test', action='store_true', help='runs Customer test')

    args = parser.parse_args()

    if args.run_test:
        c1 = Customer()
        c1.makePurchase(110)
        print(c1.discountReached())

        print()
        c1.makePurchase(60)

        print()
        print(c1.discountReached())
        print("Expected False")

        print()
        c1.makePurchase(20)

        print()
        print(c1.discountReached())
        print("Expected False")

        print()
        c1.makePurchase(90)
        print(c1.discountReached())
        print("Expected True")

customer_test()