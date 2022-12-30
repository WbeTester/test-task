from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Chrome(executable_path='C:\\Users\\strel\\PycharmProjects\\pythonselenium\\chromedriver.exe')

base_url = 'http://localhost:5000/login'
test_email = '1.test@mail.com'
test_password = '1111'

driver.get(base_url)
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(test_password)

login_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
login_button.click()
time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshotID2 ' + now_date + '.png'
driver.save_screenshot('C:\\Users\\strel\\PycharmProjects\\pythonselenium\\screen\\' + name_screenshot)


time.sleep(10)
driver.close()