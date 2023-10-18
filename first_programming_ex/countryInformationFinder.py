# Part of exercise Business P9.23:

# This programme is made to find largest population, area and density for a list/dictionary of countries:

# First for list:
# Here i find highest area, population and density when countries are sorted in a list:
# I assume the list consists of Country objects like this:
# countries = [country1, country2, country3,...]
def country_finder_for_list(list_of_countries):
    # Find largest area:
    def find_Largest_area():
        largest_country = list_of_countries[0]
        area_of_largest = largest_country.get_area()
        for c in list_of_countries:
            if c.get_area() > area_of_largest:
                largest_country = c
                area_of_largest = c.get_area()
        return largest_country
    
    # Find largest population: 
    def find_largest_population():
        largest_pop_country = list_of_countries[0]
        pop_of_largest = largest_pop_country.get_population()
        for c in list_of_countries:
            if c.get_population() > pop_of_largest:
                largest_pop_country = c
                pop_of_largest = c.get_population()
        return largest_pop_country

    # Find largest density:
    def find_largest_density():
        largest_dens = list_of_countries[0]
        dens_of_largest = largest_dens.get_density()
        for c in list_of_countries:
            if c.get_density() > dens_of_largest:
                largest_dens = c
                dens_of_largest = c.get_density()
        return largest_dens
    
    x = find_largest_population()
    y = find_Largest_area()
    z = find_largest_density()
    return x, y, z



# Now with dictionary:
# I assume that a dictionary of countries is on the form:
# country_dict = {"Country1" : [name1, population1, area1, density1], "Country2" : [name2, population2, area2, density2],...}
# Where each key is a country object
def country_finder_for_dictionary(country_dict):
    #Find largest population:
    def find_largest_population2():
        largest_population_country = list(country_dict.keys())[0]
        largest_population = largest_population_country.get_population()
        for country, data in country_dict.items():
            if data[1] > largest_population:
                largest_population_country = country
                largest_population = data[1]
        return largest_population_country

    # Find largest area:
    def find_largest_area2():
        largest_area_country = list(country_dict.keys())[0]
        largest_area = largest_area_country.get_area()
        for c, d in country_dict.items():
            if d[2] > largest_area:
                largest_area_country = c
                largest_area = d[2]
        return largest_area_country
    
    # Find highest density:
    def find_largest_density2():
        larget_density_country = list(country_dict.keys())[0]
        largest_density = larget_density_country.get_density()
        for c, d in country_dict.items():
            if d[3] > largest_density:
                larget_density_country = c
                largest_density = d[3]
        return larget_density_country

    x = find_largest_population2()
    y = find_largest_area2()
    z = find_largest_density2()
    return x, y, z