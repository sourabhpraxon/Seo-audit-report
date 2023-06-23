from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://neilpatel.com/ubersuggest/")

wait= WebDriverWait(driver,20)
ubersuggetion_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn-close"]')))
ubersuggetion_box.click()


time.sleep(10)