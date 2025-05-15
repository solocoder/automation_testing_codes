from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# If you added ChromeDriver to PATH, you can leave this simple:
driver = webdriver.Chrome()

# Open Google
driver.get("https://qa-practice.netlify.app/auth_ecommerce.html")

time.sleep(2)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("admin@admin.com")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("admin123")

submit_btn = driver.find_element(By.ID, "submitLoginBtn")
submit_btn.click()

# logout_btn = driver.find_element(By.ID, "logout")
# logout_btn.click()

time.sleep(5)
driver.quit()