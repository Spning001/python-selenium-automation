from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon Help Page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Query for cancel order')
def search_help(context):
    search_bar = context.driver.find_element(By.ID, 'helpsearch')
    search_bar.send_keys('cancel order')
    search_bar.send_keys(Keys.RETURN)


@then('Confirm search result are shown for "Cancel Items or Orders"')
def verify_help_result(context):
    expected_result = 'Cancel Items or Orders'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}."
