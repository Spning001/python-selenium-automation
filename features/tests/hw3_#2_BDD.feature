# Created by Pete Ningcharoen at 3/1/2022
Feature: Test case for cancel order in help for Amazon


  Scenario: User search for cancel order in Help
    Given Open Amazon Help Page
    When Query for cancel order
    Then Confirm search result are shown for "Cancel Items or Orders"
