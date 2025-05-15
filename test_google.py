from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# If you added ChromeDriver to PATH, you can leave this simple:
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
