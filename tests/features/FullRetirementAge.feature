Feature: Full Retirement Age Calculation

  Scenario Outline: Calculating Full Retirement Age

      Given the program is started
      When the user enters a valid "<year_choice>" year of birth
      And the user enters a valid "<month_choice>" month of birth
      Then "<retirement_age_year>" retirement age year is shown
      And "<retirement_age_month>" retirement age month is shown
      And "<retirement_date_month>" retirement date month is shown
      And "<retirement_date_year>" retirement date year is shown

      Examples: Valid Inputs
          | year_choice | month_choice | retirement_age_year | retirement_age_month | retirement_date_month | retirement_date_year |
          | 1900        | 1            | 65                  | 0                    | January               | 1965                 |
          | 1938        | 1            | 65                  | 2                    | March                 | 2003                 |
          | 1943        | 12           | 66                  | 0                    | December              | 2009                 |
          | 1955        | 12           | 66                  | 2                    | February              | 2022                 |
          | 1960        | 12           | 67                  | 0                    | December              | 2027                 |



  Scenario Outline: Entering invalid year of birth

      Given the program is started
      When the user enters an invalid "<year_choice>" year of birth
      Then "Invalid input." is shown
      And the program asks the user to enter another year of birth that is greater than or equal to 1900

      Examples: Invalid years
          | year_choice |
          | 1800        |
          | 1899        |
          | 2021        |


  Scenario Outline: Entering invalid month of birth

      Given the program is started
      And the user has entered a valid "<year_choice>" year of birth
      When the user enters an invalid "<month_choice>" month of birth
      Then "Invalid input." is shown
      And the program asks the user to enter another month of birth that is between 1 and 12

      Examples: Invalid Months
      | year_choice | month_choice |
      | 1900        | 0            |
      | 1900        | 13           |



  Scenario: Exiting the program

      Given the program is started
      And the user hasn't entered a new year of birth
      When the user presses "ENTER"
      Then the program exits
