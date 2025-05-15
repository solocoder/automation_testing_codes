from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://pro.login.cybersquare.org/cspro_login?logout=true")

submit_btn = driver.find_element(By.CLASS_NAME, "google-btn")
submit_btn.click()

time.sleep(2)
driver.quit()