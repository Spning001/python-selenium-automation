# Created by Pete Ningcharoen at 3/7/2022
Feature: Tests for Amazon Cart is Empty


  Scenario: User can confirm if Amazon Cart is Empty
    Given Open Amazon
    When Click on Cart icon
    Then Verify that "Your Amazon Cart is empty"


