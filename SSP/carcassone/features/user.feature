# Created by costefan at 12.11.15
Feature: Login for site

  Scenario: Show login form
    When I visit home page
    Then I should see login form

  Scenario: Logging with wrong data
    When I gave not valid data
    Then I see login form and see error message

  Scenario: Logging in to our system
    Given a user
    When I log in
    Then I see index page
