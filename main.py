from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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

class InstagramFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver_path)
        self.driver.get(link)
        self.main_page = 0

    def login(self):
        time.sleep(10)

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(user)

        word = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        word.send_keys(password)
        word.send_keys(Keys.ENTER)

        time.sleep(25)

        save = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
        save.click()

        time.sleep(15)

        self.main_page = self.driver.current_window_handle


    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/followers")
        time.sleep(15)

        actions = ActionChains(self.driver)



        for i in range(15):
            ActionChains(self.driver) \
                .scroll_by_amount(0, 3) \
                .perform()

    def follow(self):
        pass

igf = InstagramFollower()
igf.login()

time.sleep(5)
igf.find_followers()

