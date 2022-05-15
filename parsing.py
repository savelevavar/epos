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


def lookup(driver, query):
    driver.get("https://cabinet.permkrai.ru/login")
    try:
        button = driver.find_element_by_class_name('login__item')
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "7 признаков почему вы енот")
    time.sleep(5)
    driver.quit()