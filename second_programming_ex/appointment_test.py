import argparse
import textwrap
from appointment import Appointment, Daily, Monthly, Onetime

# Test programme for task 2/Business P10.22-P10.24.

def appointment_book_programme():
    parser = argparse.ArgumentParser(prog = "Appointment book test program", 
                                    formatter_class = argparse.RawDescriptionHelpFormatter, 
                                    description = textwrap.dedent('''\
                                                Appointment class
                                    --------------------------------
                                    The class creates instances of Appointments, the appointments consist of a description and a date.
                                    The class also holds a list of all the Appointment objects.
                                    
                                    Methods:
                                    1) save:
                                    Saves an appointment to a file where the user has their appointments.
                                    @param filename, the name of the file to save the appointment

                                    2) occursOn: 
                                    Checks if the appointment is on a date the user chooses.
                                    @param day the day of the dat
                                    @param month the month of the date
                                    @param year the year of the date
                                    
                                    3) __repr__: 
                                    @return string that represents the appointment with description and date.

                                    4) getAppointments:
                                    Class method that returns the list of all appointments.

                                    5) printAppointments:
                                    Class method to print each appointment in the appointment list

                                    6) saveAll:
                                    Class method that saves all appointments to a file.
                                    @param filename the name of the file the user want to save it to. 

                                    7) findAppointments:
                                    Class method to find all appointments on a specific date the user chooses.
                                    @param day the day of the dat
                                    @param month the month of the date
                                    @param year the year of the date

                                    8) load:
                                    Class method that reads in a file and creates Appointment objects that are added to the class list.
                                    @param filename the name of the file to read in.
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                    --------------------------------
                                    # Create Onetime appointments
                                    wash = Onetime("Wash my feet", 25, 11, 2023)
                                    tires = Onetime("Change tires", 10, 1, 2025)
                                    eat = Onetime("Eat soup", 10, 1, 2025)
                                    golf = Onetime("Play golf", 10, 1, 2020)
                                    ski = Onetime("Go skiing", 25, 10, 2023)
                                    fish = Onetime("Go fishing", 25, 11, 2023)
                                    bike = Onetime("Go biking", 25,10,2024)

                                    # Create Daily appointments:
                                    daily1 = Daily("Attend school", 10, 5, 2000)
                                    daily2 = Daily("Play playstation", 8, 11, 2023)
                                    daily3 = Daily("Football training", 20, 5, 2023)

                                    # Create Monthly appointments:
                                    monthly1 = Monthly("Dentist appointment", 7,8,2022)
                                    monthly2 = Monthly("Hairdresser appointment", 1,2,2021)
                                    monthly3 = Monthly("Doctor appointment", 13,9,2020)
                                    monthly4 = Monthly("Walk with a friend", 25,9,2020)

                                    # Write them to a file:
                                    Appointment.saveAll()

                                    # Find test:
                                    Appointment.findAppointments(25,10,2024)

                                    # Load test:
                                    Appointment.load()
                                    print("Here are all the objects created after loading the file:")
                                    Appointment.printAppointments()

                                    # Big test:
                                    # See implementation. It is huge, so would not look god to put it here.

                                    
                                    '''))
    parser.add_argument('--run_find_test', action='store_true', help='runs a find appointments test programme')
    parser.add_argument('--run_load_test', action='store_true', help='runs  a load test, where programme read from a file.')
    parser.add_argument('--run_big_test', action='store_true', help='runs  big appointment book programme with user interaction\nUser can find appointments and add appointments.')

    # Write them to a file:
    Appointment.saveAll()

    args = parser.parse_args()

    if args.run_find_test:
        wash = Onetime("Wash my feet", 25, 11, 2023)
        tires = Onetime("Change tires", 10, 1, 2025)
        eat = Onetime("Eat soup", 10, 1, 2025)
        golf = Onetime("Play golf", 10, 1, 2020)
        ski = Onetime("Go skiing", 25, 10, 2023)
        fish = Onetime("Go fishing", 25, 11, 2023)
        bike = Onetime("Go biking", 25,10,2024)

        # Daily appoinments:
        daily1 = Daily("Attend school", 10, 5, 2000)
        daily2 = Daily("Play playstation", 8, 11, 2023)
        daily3 = Daily("Football training", 20, 5, 2023)

        # Monthly appointments:
        monthly1 = Monthly("Dentist appointment", 7,8,2022)
        monthly2 = Monthly("Hairdresser appointment", 1,2,2021)
        monthly3 = Monthly("Doctor appointment", 13,9,2020)
        monthly4 = Monthly("Walk with a friend", 25,9,2020)

        Appointment.saveAll()

        Appointment.findAppointments(25,10,2024)
        print("Expected:\nOne time, Go biking, 25.10.2024\nDaily, Attend school, 10.5.2000\nDaily, Play playstation, 8.11.2023\nDaily, Football training, 20.5.2023\nMonthly, Walk with a friend, 25.9.2020")
    
    elif args.run_load_test:
        # Load test:
        Appointment.load()
        print("Here are all the objects created after loading/reading in the file:")
        Appointment.printAppointments()
        print()
        print("Expected:")
        print("Onetime, Wash my feet, 25.11.2023\nOnetime, Change tires, 10.1.2025\nOnetime, Eat soup, 10.1.2025\nOnetime, Play golf, 10.1.2020\nOnetime, Go skiing, 25.10.2023\nOnetime, Go fishing, 25.11.2023\nOnetime, Go biking, 25.10.2024\nDaily, Attend school, 10.5.2000\nDaily, Play playstation, 8.11.2023\nDaily, Football training, 20.5.2023\nMonthly, Dentist appointment, 7.8.2022\nMonthly, Hairdresser appointment, 1.2.2021\nMonthly, Doctor appointment, 13.9.2020\nMonthly, Walk with a friend, 25.9.2020")

    elif args.run_big_test:
        wash = Onetime("Wash my feet", 25, 11, 2023)
        tires = Onetime("Change tires", 10, 1, 2025)
        eat = Onetime("Eat soup", 10, 1, 2025)
        golf = Onetime("Play golf", 10, 1, 2020)
        ski = Onetime("Go skiing", 25, 10, 2023)
        fish = Onetime("Go fishing", 25, 11, 2023)
        bike = Onetime("Go biking", 25,10,2024)

        # Daily appoinments:
        daily1 = Daily("Attend school", 10, 5, 2000)
        daily2 = Daily("Play playstation", 8, 11, 2023)
        daily3 = Daily("Football training", 20, 5, 2023)

        # Monthly appointments:
        monthly1 = Monthly("Dentist appointment", 7,8,2022)
        monthly2 = Monthly("Hairdresser appointment", 1,2,2021)
        monthly3 = Monthly("Doctor appointment", 13,9,2020)
        monthly4 = Monthly("Walk with a friend", 25,9,2020)

        Appointment.saveAll()
        # Make a loop that runs untill the user tells the programme to end.
        value = False
        while not value:
            # Present the user choices:
            print("\nHere are your choices:")
            print("1 Add a new one time appoinment.")
            print("2 Add a new daily appoinment.")
            print("3 Add a new monthly appoinment.")
            print("4 Check appointments in a date")
            print("q Quit programme")
            print()

            choice = input("Write in the number of your choice: ")
            if choice == "q":
                value = True
                continue
            else:
                try:
                    choice = int(choice)

                    # # If choice = 1 or 2 or 3: Make Appointment object.
                    if choice == 1 or choice == 2 or choice == 3:
                        descript = input("Write the description of your appointment here: ")
                        date = input("Write in a date of the appointment\nFormat: day.month.year\nEx: 1st of january 2023 is equal to 1.1.2023: ")
                        date = date.strip().split(".")
                        try:
                            if len(date) == 3:
                                d = int(date[0])
                                m = int(date[1])
                                y = int(date[2])

                                if choice == 1:
                                    app = Onetime(descript, d, m, y)
                                elif choice == 2:
                                    app = Daily(descript, d, m, y)
                                else:
                                    app = Monthly(descript, d, m, y)
                                app.save()
                            else:
                                print("Wrong format of date.")
                        except ValueError as e:
                            print("Not a valid date.")
                    
                    # If Choice is 4, let the user choose a date to see if he/she has any appointments
                    elif choice == 4:
                        date_correct = False
                        while not date_correct:
                                date = input("Write in a date you want to check if you have any appointments.\nWrite q to go back to main menu.\nFormat: day.month.year\nEx: 1st of january 2023 is equal to 1.1.2023: ")
                                date = date.strip().split(".")
                                if len(date) == 1 and date[0] == 'q':
                                    date_correct = True
                                    continue
                                else:
                                    try:
                                        if len(date) == 3:
                                            d = int(date[0])
                                            m = int(date[1])
                                            y = int(date[2])
                                            date_correct = True
                                            #print(f"Appointments on: {d}.{m}.{y}:")
                                            if len(Appointment.get_appointments()) == 0:
                                                print("You have no appointments on that date.")
                                            else:
                                                Appointment.findAppointments(d, m, y)
                                        else:
                                            print("Wrong format of date.")
                                    except ValueError as e:
                                        print("Not a valid date.")
                    else:
                        print("Not a valid choice.")
                except ValueError as e:
                    print("Not a valid choice")
            
appointment_book_programme()