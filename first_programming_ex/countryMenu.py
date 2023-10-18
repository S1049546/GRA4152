# Part of exercise Business P9.23:

# # The class constructs a CountryMenu that is displayed in the terminal window
#
class CountryMenu:
    
    # # Constructor with options list. Empty when an object is initialized.
    # 
    def __init__(self):
        self._options = []
    
    # # Adds an option to the options list:
    # @param new_option the option to add
    #
    def addOption(self, new_option):
        self._options.append(new_option)
  
    # # Displays the menu, with options numbered, staring with 1. Asks the user for input. Does this until a valid input. 
    # @return number the number the user choose.
    #
    def getInput(self):
        done = False
        while not done:
            for i in range(len(self._options)):
                print("%d %s" % (i + 1, self._options[i]))
            userChoice = int(input("write in number of your choise: "))
            if userChoice >= 1 and userChoice <= len(self._options) :
                done = True 
        return userChoice