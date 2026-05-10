from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

query = "laptop"

# Open Amazon
driver.get("https://www.amazon.in")

time.sleep(3)

# Find search box
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Type laptop
search_box.send_keys(query)
elems = driver.find_elements(By.TAG_NAME, "a")

print(f"{len(elems)} elements found")

for elem in elems[:10]:
    print(elem.text)

time.sleep(5)

driver.quit()