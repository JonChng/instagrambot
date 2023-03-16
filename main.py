from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv
import os
import time

dotenv.load_dotenv()

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"

link = "https://www.instagram.com/"

driver = webdriver.Chrome(chromedriver_path)


