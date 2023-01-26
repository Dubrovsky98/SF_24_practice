#pytest -v --driver Chrome --driver-path /web_drivers/chromedriver.exe  test_selenium_simple.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time




def test_search_example(selenium):
#    driver = webdriver.Chrome(executable_path='./chromedriver')
#    driver.get('https://google.com')
    selenium.get('https://google.com')
    time.sleep(10)
    search_input = selenium.find_element(By.NAME, 'q')
    search_input.clear()
    search_input.send_keys('Мой первый тест UI')
    time.sleep(10)
    search_button = selenium.find_element(By.NAME, 'btnK')
    search_button.submit()
    time.sleep(10)
    selenium.save_screenshot('result.png')
