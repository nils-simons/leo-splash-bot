from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t


VOTE_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfl2xAE73jszk5QuRDh--bzvmUP5Pbr5vLl_IeIR4AetzfzlQ/viewform'

driver = webdriver.Chrome()
driver.get(VOTE_URL)
t.sleep(3)
elem = driver.find_element(By.CLASS_NAME, "ry3kXd")
elem.click()

t.sleep(2)

# elem = driver.find_element(By.TAG_NAME, "body")


# elem.send_keys('Leo')
# print(elem.text)

# elem.click()


# driver.execute_script("document.getElementsByClassName")

elem = driver.find_elements(By.CLASS_NAME, "LMgvRb")[87]
elem.click()

t.sleep(10)