import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import sys

LOGIN = sys.argv[1]
PASSWORD = sys.argv[2]
TOKEN = sys.argv[3]
CHAT_ID = sys.argv[4]
name_file = "img.png"

options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://vk.com/")
sleep(1)
driver.find_element(By.ID, "index_email").send_keys(LOGIN)
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(3)
driver.find_element(By.XPATH, "//span[text()='Confirm using other method']").click()
sleep(5)
driver.find_element(By.XPATH, "//span[text()='Password']").click()
sleep(3)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button/span/span").click()
sleep(3)

driver.get("https://account.habr.com/login/?consumer=career&state=bslogin")
sleep(3)
driver.find_element(By.CSS_SELECTOR, ".socials-buttons__button_vkontakte > svg").click()
sleep(5)
driver.find_element(By.XPATH, "//span/span/span").click()
sleep(5)
driver.save_screenshot(name_file)
files = {'photo': open(name_file, 'rb')}

print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())

driver.close()
