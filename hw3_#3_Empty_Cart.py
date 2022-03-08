from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path="\\Users\\pning\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

# open url
driver.get('http://www.amazon.com')
search_field = driver.find_element(By.ID, 'nav-cart-count').click()

# verify
expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2').text

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}."
print("Test case passed!!!.")