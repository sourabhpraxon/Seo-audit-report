from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
#driver.get("https://neilpatel.com/ubersuggest/")
driver.get("https://app.neilpatel.com/en/login")

wait= WebDriverWait(driver,20)

#cookie_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cookiescript_accept"]')))
#cookie_box.click()

#ubersuggetion_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn-close"]')))
#ubersuggetion_box.click()

email = driver.find_element(By.XPATH, '//*[@name="email"]')
email.send_keys("sheetal.gehlot@praxontech.com")

pwd = driver.find_element(By.XPATH, '//*[@name="password"]')
pwd.send_keys("password")

login = driver.find_element(By.XPATH, '//*[@class="sc-laZMyp htFlpD"]')
login.click()

time.sleep(10)