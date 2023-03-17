from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv
import os
import time

dotenv.load_dotenv()

user = os.environ['LOGIN']
password = os.environ['PASSWORD']
print(user)
print(password)

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"

link = "https://www.instagram.com/"

driver = webdriver.Chrome(chromedriver_path)
driver.get(link)

time.sleep(10)

username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(user)

word = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
word.send_keys(password)
word.send_keys(Keys.ENTER)

time.sleep(15)

save = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
save.click()

time.sleep(30)

notif = driver.find_element(By.XPATH, '//*[@id="mount_0_0_90"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
notif.click()

driver.quit()

