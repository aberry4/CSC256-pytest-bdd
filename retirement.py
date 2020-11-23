class Retirement:
    def __init__(self, year_choice):
        self.year_choice = year_choice
        self.month_choice = None
        self.retirement_age_year = None
        self.retirement_age_month = None
        self.retirement_date_year = None
        self.retirement_date_month = None
        self.month_to_string = None

    def get_age(self):
        year_choice = self.date_validation(self.year_choice, "year")
        month_choice = self.date_validation(input("Enter the month of birth: "), "month")
        self.year_choice, self.month_choice = year_choice, month_choice

    def retirement_age_calc(self):
        retirement_age_month = 0
        year_choice = self.year_choice
        if year_choice < 1943:
            retirement_age_year = 65
            if year_choice > 1937:
                retirement_age_month = (year_choice - 1937) * 2
        elif year_choice < 1960:
            retirement_age_year = 66
            if year_choice > 1954:
                retirement_age_month = (year_choice - 1954) * 2
        else:
            retirement_age_year = 67
        self.retirement_age_year, self.retirement_age_month = retirement_age_year, retirement_age_month

    def retirement_date_calc(self):
        retirement_date_year = self.year_choice + self.retirement_age_year
        retirement_date_month = self.month_choice + self.retirement_age_month
        if retirement_date_month > 12:
            retirement_date_year += 1
            retirement_date_month -= 12
        self.retirement_date_year, self.retirement_date_month = retirement_date_year, retirement_date_month

    def convert_month_to_string(self, month_number):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        self.month_to_string = months[month_number - 1]

    def calculate_retirement(self):
        self.get_age()
        self.retirement_age_calc()
        self.retirement_date_calc()
        self.convert_month_to_string(self.retirement_date_month)

    def __str__(self):
        self.calculate_retirement()
        return "Your full retirement age is " + str(self.retirement_age_year) + " and " + str(
            self.retirement_age_month) + " months\n" + "This will be in " + self.month_to_string + " of " + str(
            self.retirement_date_year) + "\n"


def date_validation(number, date_type):
    while True:
        number = number.strip()
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Please enter a number")
            if date_type == "year":
                number = input("Enter the year of birth: ")
            else:
                number = input("Enter the month of birth: ")
            continue
        if date_type == "year" and number < 1900:
            number = input("Invalid input.\nPlease enter a year greater than or equal to 1900: ")
            continue
        elif date_type == "year" and number > 2020:
            number = input("Invalid input.\nPlease enter a year less than or equal to 2020: ")
            continue
        elif date_type == "month" and (number > 12 or number < 1):
            number = input("Invalid input.\nPlease enter a month between 1 and 12: ")
            continue
        else:
            break
    return number
