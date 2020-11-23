
from retirement import Retirement


def main():
    print("Social Security Full Retirement Age Calculator")
    user_choice = get_user_choice()
    while user_choice:
        retirement1 = Retirement(user_choice)
        print(retirement1)
        user_choice = get_user_choice()


def get_user_choice():
    user_choice = validate_user_choice(input("Enter the year of birth or press 'enter' to exit: "))
    return user_choice


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

if __name__ == "__main__":
    main()
