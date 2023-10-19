# Task P9.23: 

# # The class holds information about a country, the information is name of the country, population, area and density.
# 
class Country:

    # # Constructs an object of a country, with name, population and area as parameters. 
    #
    def __init__(self, name, population, area):
        self._name = name
        self._population = population
        self._area = area
        self._density = float(self._population / self._area)
    
    # # returns the name of the country
    # @return self._name instance variable that is the name of the country
    #
    def get_name(self):
        return self._name
    
    # # returns the population of the country
    # @return self._population instance variable that is the population of the country
    #
    def get_population(self):
        return self._population

    # # returns the area of the country
    # @return self._area instance variable that is the area of the country
    #
    def get_area(self):
        return self._area

    # # returns the density of the country
    # @return self._density instance variable that is the density of the country
    #
    def get_density(self):
        return self._density