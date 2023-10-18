# task Business P9.26:

# # The class holds information about a customers purchaes and if he/she has a discount to use
#
class Customer:
    
    # # Constructor:
    # initiates an instance of the Customer class:
    # Self value is the amount the customer has shopped for. Everytime the customer has spent 100$ it goes back to 0.
    def __init__(self):
        self._value = 0
        self._has_discount = False

    # # Makes a purchase for a customer
    # @param amount price of the purchase
    def makePurchase(self, amount):
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        
        if self._has_discount:
            amount -= 10
            self._has_discount = False

        self._value += amount

        if self._value >= 100:
            self._has_discount = True
            self._value -= 100
            print("You have a discount, so your next purchase will get a $10 discount.")

        print("The price is", amount)
    
    # # Checks if customer has a discount
    # @return boolean, if the customer has a discount to use or not.
    def discountReached(self):
        return self._has_discount