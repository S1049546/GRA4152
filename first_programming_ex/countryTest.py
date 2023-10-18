# Part of exercise Business P9.23:

# # 
# Test program for the Country class, countryInformationFinder programme and the CountryMenu class:
#
def country_test():
    from country import Country
    from countryInformationFinder import country_finder_for_list
    from countryInformationFinder import country_finder_for_dictionary
    from countryMenu import CountryMenu
    import argparse
    import textwrap
    parser = argparse.ArgumentParser(prog = "Customer test program", 
                                    formatter_class = argparse.RawDescriptionHelpFormatter, 
                                    description = textwrap.dedent('''\
                                                CountryMenu
                                    --------------------------------
                                    THe class displays a Menu in the terminal for the user.
                                    
                                    Methods:
                                    1) addOption: 
                                    @param new_option the new string/option that is to be added to the option list
                                    
                                    2) getInput: 
                                    @return userChoice the choice (int) that the user wrote in as input.
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                    --------------------------------
                                    norway = Country("Norway", 5000000, 10000000)               # Make countries
                                    country_list = [norway, sweden, denmark]                    # Put them in a list
                                    menu = CountryMenu()                                        # Initiate a Menu
                                    list_stats = country_finder_for_list(country_list)          # Get the highest pop, area and density for when using list
                                    print(list_stats)                                           # print the stats
                                    list_stats = country_finder_for_dictionary(country_dict)    # Get the highest pop, area and density when using a dict
                                    print(list_stats)                                           # print the stats
                                    '''))
    parser.add_argument('--run_test', action='store_true', help='runs Customer test')
    #parser.add_argument('-- list', type = str, action = 'store_True', help = "Here you choose if you want to use a list of countries or a dictionary of counries")

    args = parser.parse_args()

    if args.run_test:
        # Countries:
        norway = Country("Norway", 5000000, 20000000)
        sweden = Country("Sweden", 10000000, 15000000)
        denmark = Country("Denmark", 3000000, 4000000)   

        # list of countries:
        country_list = [norway, sweden, denmark]

        # dictionary of countries:
        country_dict = {norway : [norway.get_name(), norway.get_population(), norway.get_area(), norway.get_density()],
                        sweden : [sweden.get_name(), sweden.get_population(), sweden.get_area(), sweden.get_density()],
                        denmark : [denmark.get_name(), denmark.get_population(), denmark.get_area(), denmark.get_density()]}
        
        # CountryMenu object:
        menu = CountryMenu()

        # Add relevant options for this exercise:
        menu.addOption("Find country with the largest Population")
        menu.addOption("Find country with the largest area")
        menu.addOption("Find country with the largest population density")
        menu.addOption("Quit")
        
        print("Options to choose from:")
        choice = menu.getInput()
        print()

        # For list:
        list_stats = country_finder_for_list(country_list)
        print("List format:")
        if choice == 1:
            print("Country with largest population:", list_stats[0].get_name(), " with a population of ", list_stats[0].get_population(), "people.")
            print("Expected: Sweden")
        elif choice == 2:
            print("Country with largest area:", list_stats[1].get_name(), " with an area of ", list_stats[1].get_area(), "km2.")
            print("Expected: Norway")
        elif choice == 3:
            print("Country with largest population density:", list_stats[2].get_name(), " with a density of ", list_stats[2].get_density(), ".")
            print("Expected: Denmark")
        else:
            pass
    
        # For dictionary:
        list_stats = country_finder_for_dictionary(country_dict)
        print()
        print("Dictionary format:")
        if choice == 1:
            print("Country with largest population:", list_stats[0].get_name(), " with a population of ", list_stats[0].get_population(), "people.")
            print("Expected: Sweden")
        elif choice == 2:
            print("Country with largest area:", list_stats[1].get_name(), " with an area of ", list_stats[1].get_area(), "km2.")
            print("Expected: Norway")
        elif choice == 3:
            print("Country with largest population density:", list_stats[2].get_name(), " with a density of ", list_stats[2].get_density(), ".")
            print("Expected: Denmark")
        else:
            pass
        print("programme finished!")

if __name__ == '__main__':
 country_test()  