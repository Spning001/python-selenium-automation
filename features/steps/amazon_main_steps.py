from selenium.webdriver.common.by import By
from behave import given, when, then

# WHEN A CODE IS BEING REFERENCED IN MANY STEPS, USE SEARCH_INPUT
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('http://www.amazon.com')


@when('Search for {keyword}')
def search_product(context, keyword):
    context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()



