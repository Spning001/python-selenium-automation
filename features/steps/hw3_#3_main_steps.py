from selenium.webdriver.common.by import By
from behave import given, when, then


# already defined
# @given('Open Amazon')
# def open_amazon(context):
#     context.driver.get('http://www.amazon.com')


@when('Click on Cart icon')
def cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify that "Your Amazon Cart is empty"')
def verify_cart_result(context):
        expected_result = 'Your Amazon Cart is empty'
        actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2').text
        assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}."