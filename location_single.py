from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
query = "laptop"

driver.get(f"https://amazone.net/en-in")
elem = driver.find_element(By.CLASS_NAME, "cmpboxrecall cmpstyleroot")
print(elem.get_attribute("outerHTML"))
elem.send_keys(query)
time.sleep(5)



driver.close()