# Assignment 2:
# Task 2:
# Task Business P10.22 - Business P10.24
# Docstring is in this file.
class Appointment:
    """
    # # Super class Appointment, a class that can make appointment objects and hold them in a list.
    # Holds a class variable _appoinmtents that contains all appointments.
    #
    """

    """
    # # This is a class variable that holds all the appointments that are created. 
    #
    """
    _appointments = []

    def __init__(self, description, day, month, year):
        """
        # # Constructor that creates instances of Appointments
        # @param description the description of the appointment
        # @param day of the date
        # @param month of the date
        # @param year of the date
        #
        """
        self._description = description
        self._month = month
        self._day = day
        self._year = year
        Appointment._appointments.append(self)
    
    def save(self, filename="appointments.csv"):
        """
        # # This method adds/saves an appointment in the class variable.
        # @param filename the name of the faile to save it to. Default appointments.csv
        #
        """
        with open(filename, "a") as f:
            f.write(f"{repr(self)}\n")
    
    def occursOn(self, day, month, year):
        """
        # # Method that checks if the appointment happens on a specific date. If same returns True.
        # In the super class, if all parts of the date are correct the method returns True.
        # @param day the day
        # @param month the month
        # @param year the year
        # @return boolean if it is true or not
        #
        """
        if (year == self._year) & (month == self._month) & (day == self._day):
            return True
        return False
    
    def __repr__(self):
        """
        # # This method is created to be used in the subclasses. each subclass has a different implementation.
        # So here it is declared, so that with the same method call, each subclass implements differently. 
        #
        """
        raise NotImplementedError
    
    @classmethod
    def get_appointments(cls):
        """
        # # Class method to return the list of appointments.
        # @return _appointments the list of appointments
        #
        """
        return Appointment._appointments
    
    @classmethod 
    def printAppointments(cls):
        """
        # # Class method to print out each Appointment in the class variable list.
        # 
        """
        for a in Appointment._appointments:
            print(a)
    
    @classmethod
    def saveAll(cls, filename = 'appointments.csv'):
        """
        # # Class method to save all the appointments to a file:
        # This is so that I do not need to manually do it one by one.
        #
        """
        try:
            with open(filename, "w") as f: # This one is just to reset the content of the file after each time the program runs.
                # So that we dont end up having multiple of the same content in the csv file.
                # I have done this so that the find test works. If not we would end up printing out the same appointment 2 times if we do the test 2 times. and 3 on the third...
                # Usually a user can choose file name their selves, and then it is not really a problem. 
                f.write("")
        except FileExistsError:
            pass
        for a in Appointment._appointments:
            a.save(filename)
    
    @classmethod
    def findAppointments(cls, day, month, year):
        """
        # # Class method that goes through the list of appointments and writes out all appointments on a date.
        #
        """
        print(f"Appointments on {day}.{month}.{year}:")
        for a in Appointment._appointments:
            if a.occursOn(day, month, year):
                print(a)

    @classmethod
    def load(cls, filename = "appointments_to_load.csv"):
        """
        # # Class method that reads in a file and creates Appointment objects that are added to the class list.
        #
        """
        with open(filename, "r") as f:
            for line in f:
                list = line.strip().split(",")
                if len(list) != 3:
                    raise ValueError("Line is not in the correct format: 'Type, Description, Date'")
                try:
                    CLASS = list[0]
                    des = list[1]
                    date = list[2]
                    date_list = date.split(".")
                    d = date_list[0]
                    m = date_list[1]
                    y = date_list[2]

                    if CLASS == 'Onetime':
                        obj = Onetime(des, d, m, y)
                    elif CLASS == 'Daily':
                        obj = Daily(des, d, m, y)
                    elif CLASS == 'Monthly':
                        obj = Monthly(des, d, m, y)
                    else:
                        print("Could not load an make object")
                except IndexError:
                    print("Line doesn't have enough values:", line)
                except ValueError:
                    print("Date values must be integers:", line)
                except AttributeError:
                    print(f"Error creating object from line: {line}")



    
class Daily(Appointment):
    """
    # # Subclass Daily that extends the superclass Appointment.
    #
    """
    def __init__(self, description, start_day, start_month, start_year):
        """
        # # Constructor method that initializes a Daily object.
        # @param description the description of the Daily object
        # @param start_day the day the appointments starts
        # @param start_month the month the appointments starts
        # @param start_year the year the appointments starts
        #
        """
        super().__init__(description, start_day, start_month, start_year)
       
    def occursOn(self, day, month, year):
        """
        # # Checks if there is any appointments on the date you input.
        # The method overrides the Superclass method from Appointment to work for the subclass.
        # In this subclass it is not enough to use same implementation as in the super class.
        # Here we need to do more checks. Because we need to be able to return True for all dates/days after the beginning of the appointment. 
        # @param day the date
        # @param month the date
        # @param year the date
        # @return boolean if it is true or not
        #
        """
        if year >= self._year:
            return True
        elif year == self._year:
            if month >= self._month:
                return True
            elif month == self._month:
                if day >= self._day:
                    return True
        return False

    def __repr__(self):
        """
        # # A string representation of the  daily appointment, with description and date.
        #
        """
        return f"Daily, {self._description}, {self._day}.{self._month}.{self._year}"

class Monthly(Appointment):
    """
    # # Subclass Monthly that extends the superclass Appointment
    #
    """

    def __init__(self, description, start_day, start_month, start_year):
        """
        # # Constructor that initializes a Monthly object.
        # @param description the description of the Monthly object
        # @param start_day the day the appointments starts
        # @param start_month the month the appointments starts
        # @param start_year the year the appointments starts
        #
        """
        super().__init__(description, start_day, start_month, start_year)

    def occursOn(self, day, month, year):
        """
        # # Checks if there is any appointments on the date you input.
        # The method overrides the Superclass method from Appointment to work for the subclass Monthly.
        # In this subclass it is not enough to use same implementation as in the super class.
        # Here we need to do more checks than in the Superclass method. 
        # Because we need to be able to return True for all dates for every month after the appointment starts. 
        # @param day the date
        # @param day the date
        # @param month the date
        # @param year the date
        # @return boolean true if it is the same
        #
        """
        if year >= self._year:
            if month >= self._month:
                if day == self._day:
                    return True
        return False

    def __repr__(self):
        """
        # # A string representation of the monthly appointment, with description and date.
        #
        """
        return f"Monthly, {self._description}, {self._day}.{self._month}.{self._year}"
    
class Onetime(Appointment):
    """
    # # Subclass Onetime that extends the superclass Appointment
    #
    """
    def __init__(self, description, year, month, day):
        """
        # # Constructor that constructs an Onetime object.
        # @param description the description of the Onetime appointment
        # @param day the date
        # @param month the date
        # @param year the date
        #
        """
        super().__init__(description, year, month, day)

    def __repr__(self):
        """
        # # A string representation of the Onetime appointment, with description and date.
        #
        """
        return f"Onetime, {self._description}, {self._day}.{self._month}.{self._year}"
    
        """
        # The method occursOn() does not need to change in the subclass Onetime from the superclass Appointment.
        """

        # Question 5 in task 2:
        """
        In my approach I use inheritance in the save method, that means that I create it in the superclass an let the subclasses 
        use the same implementation. If I were to use polymorphism I would still implement it in the Superclass, 
        but then implement it differently in each subclass to fit each class specific need.
        """