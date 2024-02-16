from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_option)
driver.get("http://the-internet.herokuapp.com/login")

username_element = driver.find_element(By.ID, 'username')
username_element.send_keys('tomsmith')

password_element = driver.find_element(By.ID, 'password')
password_element.send_keys('SuperSecretPassword!')

message_element = driver.find_element(By.CLASS_NAME, 'subheader')
print(message_element.text)

time.sleep(5)
driver.close()