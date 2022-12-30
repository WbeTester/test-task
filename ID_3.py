from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Chrome(executable_path='C:\\Users\\strel\\PycharmProjects\\pythonselenium\\chromedriver.exe')

base_url = 'http://localhost:5000/signup'
test_email = '2.test@mail.com'
test_name = 'Test'

driver.get(base_url)
driver.maximize_window()

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
name = driver.find_element(By.XPATH, "//input[@type='text']")
name.send_keys(test_name)

sign_up_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
sign_up_button.click()
time.sleep(5)

"""авторизуемся после регистрации"""

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
login_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
login_button.click()
time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshotID3 ' + now_date + '.png'
driver.save_screenshot('C:\\Users\\strel\\PycharmProjects\\pythonselenium\\screen\\' + name_screenshot)


time.sleep(10)
driver.close()