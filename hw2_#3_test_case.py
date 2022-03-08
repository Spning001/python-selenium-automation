from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path="\\Users\\pning\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

# open url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# search for Cancel order
search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('cancel order')
search_field.send_keys(Keys.RETURN)
# can be combined to read as such
# search_field = driver.find_element(By.ID, 'helpsearch'),send_keys('cancel order'), Keys.RETURN

# verify
expected_result = 'Cancel Items or Orders'
# using XPATH and connecting <div and <h1>
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}."
print("Test case passed.")

#driver.quit()
