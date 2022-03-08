from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@then('Verify search result are shown for {expected_result}')
def verify_result(context, expected_result):
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}."
