#hw3_1_CSS_locators

#Amazon logo by Class
driver.find_element(By.CSS_SELECTOR, '.a-link-nav-icon')

#Create account by Class
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Your name by ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Email by ID
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Password by ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Passwords must be at least 6 charaters by Class
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini')

#Re-enter password field by ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Continue button by ID
driver.find_element(By.CSS_SELECTOR, '#continue')

#Conditions of Use by partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

#Privacy Notice by partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#Sign in link by partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='0&openid.return_to']")