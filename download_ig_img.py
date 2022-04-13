from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget


# variables
USERNAME = input('username? ')
PASSWORD = input('password? ')
KEYWORD = input('keyword? ')


# initialize driver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# wait web loading
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'username'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)

# XPATH of logic in button
login = driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')


# do action
username.clear()  # clean username query
password.clear()  # clean password query
username.send_keys(USERNAME)  # send username
password.send_keys(PASSWORD)  # send password
login.click()  # click login

# wait search query
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

keyword = KEYWORD
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

# wait img loading
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
)

# driver
for i in range(1):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)

imgs = driver.find_elements(by=By.CLASS_NAME, value='FFVAD')

path = os.path.join(keyword)

# madir folder
os.mkdir(path)

for counter, img in enumerate(imgs):
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(img.get_attribute('src'), save_as)
