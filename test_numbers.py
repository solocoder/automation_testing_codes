
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

# If you added ChromeDriver to PATH, you can leave this simple:
driver = webdriver.Chrome()

# Open Google
driver.get("https://bugeater.web.app/app/list")

time.sleep(2)

wait = WebDriverWait(driver, 10)

accept_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > button.btn.btn-primary")
accept_btn.click()

ch1_1 = driver.find_element(By.LINK_TEXT, "Challenge #1.1: Number Addition").click()

skip_btn = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='button-skip']")
skip_btn.click()

chData_1 = driver.find_element(By.ID, "first")
chData_1.click()
chData_1.send_keys("1")

chData_2 = driver.find_element(By.ID, "second")
chData_2.click()
chData_2.send_keys("2")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(3)

chData_1.clear()
chData_1.send_keys("-2")

chData_2.clear()
chData_2.send_keys("4")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)

chData_1.clear()
chData_1.send_keys("1.5")

chData_2.clear()
chData_2.send_keys("2.5")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)

chData_1.clear()
chData_1.send_keys("abc")

chData_2.clear()
chData_2.send_keys("1")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_2.clear()

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)

chData_1.clear()
chData_1.send_keys("10000000000")

chData_2.clear()
chData_2.send_keys("1")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(3)

# NEXT CHALLENGE BUTTON
next_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer a.btn.btn-primary")
next_btn.click()

time.sleep(3)

chData_1.clear()
chData_1.send_keys("4")

chData_2.clear()
chData_2.send_keys("2")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)

chData_1.clear()
chData_1.send_keys("-10")

chData_2.clear()
chData_2.send_keys("2")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)

chData_1.clear()
chData_1.send_keys("5")

chData_2.clear()
chData_2.send_keys("2")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)

chData_1.clear()
chData_1.send_keys("abc")

chData_2.clear()
chData_2.send_keys("1")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)
chData_1.clear()
chData_2.clear()

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)
chData_1.send_keys("10")
chData_2.send_keys("0")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(2)
next_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer a.btn.btn-primary")
next_btn.click()

time.sleep(2)

chData_1.clear()
chData_1.send_keys("P@ssw0rD")

calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("hElloW0rld")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("Passw0rd!7")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
calculateBtn.click()

time.sleep(1)
chData_1.send_keys("Mo7%")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("asdfghjklpoiuytrewq")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("ONLYCAPITAL")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("onlylower")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("001122")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("@@@@@")
calculateBtn.click()

time.sleep(1)
chData_1.clear()
chData_1.send_keys("Κωδικός")
calculateBtn.click()

time.sleep(2)

next_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > a.btn.btn-primary")
next_btn.click()

# CHALLENGE 4

time.sleep(2)

chData_1.clear()
chData_1.send_keys("skyline7")
chData_2 = driver.find_element(By.ID, "second")
chData_2.clear()
chData_2.send_keys("Michael")
chData_3 = driver.find_element(By.ID, "third")
chData_3.send_keys("Henderson")
calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()



time.sleep(1)

chData_1.clear()
chData_1.send_keys("k_3")
chData_2.clear()
chData_2.send_keys("J")
chData_3.clear()
chData_3.send_keys("Z")
calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()


time.sleep(1)

chData_1.clear()
chData_1.send_keys("longnick9_")
chData_2.clear()
chData_2.send_keys("MaximilianaElizabethMontgomery")
chData_3.clear()
chData_3.send_keys("AlexanderHamiltonJeffersonSmith")
calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()


time.sleep(1)

chData_1.clear()
chData_2.clear()
chData_3.clear()
calculateBtn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit']")
calculateBtn.click()

time.sleep(1)

chData_1.send_keys("123-AA")
chData_2.send_keys("X Æ A-12")
chData_3.send_keys("X Æ A-12")
calculateBtn.click()

time.sleep(1)

chData_1.clear()
chData_1.send_keys("@@@@@")
chData_2.clear()
chData_2.send_keys("Christopher")
chData_3.clear()
chData_3.send_keys("Williams")
calculateBtn.click()
time.sleep(3)

next_btn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > a.btn.btn-primary")
next_btn.click()



# clrBtn = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > button.btn.btn-primary")
# clrBtn.click()
 

input("Press Enter to exit and close the browser...")
