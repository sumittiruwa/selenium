from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome
driver = webdriver.Chrome()

# Open LinkedIn Jobs
driver.get("https://www.linkedin.com/jobs")

time.sleep(5)

# Find search box
search = driver.find_element(
    By.CSS_SELECTOR,
    "input[aria-label='Search by title, skill, or company']"
)

# Search internships
search.send_keys("Internship Kathmandu")
search.send_keys(Keys.RETURN)

time.sleep(5)

# Get internship titles
jobs = driver.find_elements(By.CSS_SELECTOR, ".base-search-card__title")

print("\nInternships Found:\n")

for job in jobs[:10]:
    print(job.text)

input("\nPress Enter to close browser...")

driver.quit()