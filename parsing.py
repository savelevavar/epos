import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome('C:/Users/ACER/Downloads/chromedriver_win32/chromedriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver):
    driver.get("https://cabinet.permkrai.ru/login")
    login = 'varya.saveleva.05@mail.ru'
    password = 'qweasdzxc2289'
    try:
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "login__item")))
        button.click()
        box_login = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "base-input login__input login__input--login")))
        box_password = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "base-input login__input login__input--password")))

        box_login.send_keys(login)
        box_password.send_keys(password)
    except TimeoutException:
        print("Box or Button not found in epos")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    # driver.quit()