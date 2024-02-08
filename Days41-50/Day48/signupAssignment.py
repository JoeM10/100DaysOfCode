from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keeps the window open.
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://secure-retreat-92358.herokuapp.com")

firstName = driver.find_element(By.CSS_SELECTOR, '[name="fName"]')
firstName.send_keys("Joe")

lastName = driver.find_element(By.CSS_SELECTOR, '[name="lName"]')
lastName.send_keys("Shmo")

email = driver.find_element(By.CSS_SELECTOR, '[name="email"]')
email.send_keys("testing@123.com")

signUpButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
signUpButton.click()

# Closes the window
# driver.quit()