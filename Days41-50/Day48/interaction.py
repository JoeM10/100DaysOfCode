from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keeps window open. 
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articleAmount = driver.find_element(By.CSS_SELECTOR, "[title='Special:Statistics']")
print(articleAmount.text)

# Click on things
# articleAmount.click()

# Find the "Search" <input> by name.
search = driver.find_element(By.NAME, value="search")

# Send keyboard input.
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# Closes the window
# driver.quit()