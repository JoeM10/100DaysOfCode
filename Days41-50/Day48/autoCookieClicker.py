from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta

# Keeps window open. 
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

selectEnglish = driver.find_element(By.CSS_SELECTOR, "[id='langSelect-EN']")
selectEnglish.click()
time.sleep(5)
bigCookie = driver.find_element(By.CSS_SELECTOR, "[id='bigCookie']")

delta = timedelta(seconds=5)
while True:
  clicking = True
  currentTime = datetime.now()
  futureTime = currentTime + delta
  try:
    purchasableUpgrades = driver.find_elements(By.CSS_SELECTOR, "[class='product unlocked enabled']")
    purchaseUpgrade = purchasableUpgrades[-1]
    purchaseUpgrade.click()
  except:
    pass

  while clicking:
    now = datetime.now()
    bigCookie.click()
    if now >= futureTime:
      clicking = False

