from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Chrome(executable_path='C:\\Users\\strel\\PycharmProjects\\pythonselenium\\chromedriver.exe')

base_url = 'http://localhost:5000/signup'
test_email = '&#$%^*@mail.com'
test_email_2 = ' '
test_name = ' '
test_name_2 = '&#$%^*'
test_password = ' '
test_password_2 = '&#$%^*'

driver.get(base_url)
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
name = driver.find_element(By.XPATH, "//input[@type='text']")
name.send_keys(test_name)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(test_password)

sign_up_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
sign_up_button.click()
time.sleep(5)

"""авторизуемся после регистрации"""

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(test_password)

login_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
login_button.click()
time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshotID5.1 ' + now_date + '.png'
driver.save_screenshot('C:\\Users\\strel\\PycharmProjects\\pythonselenium\\screen\\' + name_screenshot)

"""разлогиниваемся, чтобы зарегистрироваться под новыми данными"""

log_out_button = driver.find_element(By.XPATH, "//a[@href='/logout']")
log_out_button.click()
time.sleep(5)
sign_up_button = driver.find_element(By.XPATH, "//a[@href='/signup']")
sign_up_button.click()

"""Регистрируемся под вторыми данными"""

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email_2)
name = driver.find_element(By.XPATH, "//input[@type='text']")
name.send_keys(test_name_2)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(test_password_2)

sign_up_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
sign_up_button.click()
time.sleep(5)

name_screenshot_2 = 'screenshotID5.2 ' + now_date + '.png'
driver.save_screenshot('C:\\Users\\strel\\PycharmProjects\\pythonselenium\\screen\\' + name_screenshot_2)


time.sleep(5)
driver.close()
