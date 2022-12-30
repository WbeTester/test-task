from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\strel\\PycharmProjects\\pythonselenium\\chromedriver.exe')

base_url = 'http://localhost:5000/'
test_email = '1.test@mail.com'
test_password = '1111'

driver.get(base_url)
driver.maximize_window()

sign_up_button = driver.find_element(By.XPATH, "//a[@href='/signup']")
sign_up_button.click()

email = driver.find_element(By.XPATH, "//input[@name='email']")
email.send_keys(test_email)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(test_password)

sign_up_button = driver.find_element(By.XPATH, "//button[@class='button is-block is-info is-large is-fullwidth']")
sign_up_button.click()


time.sleep(10)
driver.close()