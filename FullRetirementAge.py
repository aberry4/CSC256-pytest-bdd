def main():
    print("Social Security Full Retirement Age Calculator")
    user_choice = get_user_choice()
    while user_choice:
        year_choice, month_choice = get_age(user_choice)
        retirement_age_year, retirement_age_month = retirement_age_calc(year_choice)
        retirement_date_year, retirement_date_month = retirement_date_calc(year_choice, month_choice,
                                                                           retirement_age_year, retirement_age_month)
        output(retirement_age_year, retirement_age_month, retirement_date_year, retirement_date_month)
        user_choice = get_user_choice()


def get_user_choice():
    user_choice = validate_user_choice(input("Enter the year of birth or press 'enter' to exit: "))
    return user_choice


def get_age(year_choice):
    year_choice = date_validation(year_choice, "year")
    month_choice = date_validation(input("Enter the month of birth: "), "month")
    return year_choice, month_choice


def retirement_age_calc(year_choice):
    retirement_age_month = 0
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
    return retirement_age_year, retirement_age_month


def retirement_date_calc(user_age_year, user_age_month, retirement_age_year, retirement_age_month):
    retirement_date_year = user_age_year + retirement_age_year
    retirement_date_month = user_age_month + retirement_age_month
    if retirement_date_month > 12:
        retirement_date_year += 1
        retirement_date_month -= 12
    return retirement_date_year, retirement_date_month


def convert_month_to_string(month_number):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return months[month_number - 1]


def output(retirement_age_year, retirement_age_month, retirement_date_year, retirement_date_month):
    print("Your full retirement age is", retirement_age_year, "and", retirement_age_month, "months")
    print("This will be in", convert_month_to_string(retirement_date_month), "of", retirement_date_year)
    print()


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


def validate_user_choice(user_choice):
    validated = False
    user_choice = user_choice.strip()
    while not validated:
        if user_choice and not user_choice.isnumeric():
            print("Invalid input")
            user_choice = input("Enter the year of birth or press 'enter' to exit: ")
        else:
            validated = True
    return user_choice

main()
