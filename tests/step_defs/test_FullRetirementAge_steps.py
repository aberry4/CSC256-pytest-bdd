from pytest_bdd import given, when, then, scenarios, parsers
from functools import partial
from retirement import date_validation
from RetirementCalculator import *


EXTRA_TYPES = {
    'Number': int,
    'String': str,
}

CONVERTERS = {
    'year_choice': str,
    'month_choice': str,
    'retirement_age_year': int,
    'retirement_age_month': int,
    'retirement_date_month': str,
    'retirement_date_year': int,
}
parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


scenarios('../features/FullRetirementAge.feature', example_converters=CONVERTERS)


@given("the program is started")
def step_impl():
    pass


@when(parsers.cfparse('the user enters a valid "{year_choice}" year of birth'))
@when('the user enters a valid "<year_choice>" year of birth')
def age_calc(year_choice):
    date_validation(year_choice, "year")
    return Retirement(year_choice=year_choice)


@when(parsers.cfparse('the user enters a valid "{month_choice}" year of birth'))
@when('the user enters a valid "<month_choice>" month of birth')
def set_month(age_calc, month_choice):
    date_validation(month_choice, "month")
    age_calc.month_choice = month_choice


@then(parsers.cfparse('"{retirement_age_year:Number}" retirement age year is shown', extra_types=EXTRA_TYPES))
@then('"<retirement_age_year>" retirement age year is shown')
def check_retirement_age_year(age_calc, retirement_age_year):
    age_calc.calculate_retirement()
    assert age_calc.retirement_age_year == retirement_age_year


@then(parsers.cfparse('"{retirement_age_month:Number}" retirement age month is shown', extra_types=EXTRA_TYPES))
@then('"<retirement_age_month>" retirement age month is shown')
def check_retirement_age_month(age_calc, retirement_age_month):
    age_calc.calculate_retirement()
    assert age_calc.retirement_age_month == retirement_age_month


@then(parsers.cfparse('"{retirement_date_month:String}" retirement date month is shown', extra_types=EXTRA_TYPES))
@then('"<retirement_date_month>" retirement date month is shown')
def check_retirement_date_month(age_calc, retirement_date_month):
    age_calc.calculate_retirement()
    assert age_calc.month_to_string == retirement_date_month


@then(parsers.cfparse('"{retirement_date_year:Number}" retirement date year is shown', extra_types=EXTRA_TYPES))
@then('"<retirement_date_year>" retirement date year is shown')
def check_retirement_date_year(age_calc, retirement_date_year):
    age_calc.calculate_retirement()
    assert age_calc.retirement_date_year == retirement_date_year

@when(parsers.cfparse('the user enters an invalid "{year_choice:String}" year of birth', extra_types=EXTRA_TYPES))
@when('the user enters an invalid "<year_choice>" year of birth')
def enter_invalid_year(year_choice):
    validate_user_choice(user_choice=year_choice)


@then('"Invalid input." is shown')
def check_output(capfd):
    captured = capfd.readouterr()
    assert "Invalid input." in captured.out


@then("the program asks the user to enter another year of birth that is greater than or equal to 1900")
def check_ask_new_year(capfd):
    captured = capfd.readouterr()
    assert "Enter the year of birth or press 'enter' to exit: " in captured.out

@given(parsers.cfparse('the user has entered a valid "{year_choice:String}" year of birth', extra_types=EXTRA_TYPES))
@given('the user has entered a valid "<year_choice>" year of birth')
def enter_valid_year(year_choice):
    date_validation(year_choice, 'year')
    ret = Retirement(year_choice=year_choice)
    return ret


@when(parsers.cfparse('the user enters an invalid "{month_choice:String}" month of birth', extra_types=EXTRA_TYPES))
@when('the user enters an invalid "<month_choice>" month of birth')
def enter_invalid_month(month_choice):
    date_validation(month_choice, 'month')


@then("the program asks the user to enter another month of birth that is between 1 and 12")
def check_invalid_month_message(capfd):
    captured = capfd.readouterr()
    assert "Invalid input.\nPlease enter a month between 1 and 12: " in captured.out


@given("the user hasn't entered a new year of birth")
def restart():
    main()


@when('the user presses "ENTER"')
def press_enter(monkeypatch, capfd):
    captured = capfd.readouterr()
    monkeypatch.setattr('builtins.input', lambda _: '')


@then("the program exits")
def step_impl():
    assert SystemExit


