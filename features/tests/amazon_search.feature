# Created by Pete Ningcharoen at 2/23/2022
Feature: Tests for Amazon search
  # Enter feature description here (optional)

  Scenario: User can search for a coffee
    Given Open Amazon
    When Search for coffee
    Then Verify search result are shown for "coffee"

  Scenario: User can search for a table
    Given Open Amazon
    When Search for table
    Then Verify search result are shown for "table"