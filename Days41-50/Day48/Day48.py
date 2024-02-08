from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps the window open.
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.python.org")

eventTimes = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
eventNames = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = [{"time": time.text, "name": name.text} for time, name in zip(eventTimes, eventNames)]
print(events)

# Closes the window.
driver.quit()