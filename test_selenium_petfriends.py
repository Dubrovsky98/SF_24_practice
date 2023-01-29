#python -m pytest -v --driver Chrome --driver-path /web_drivers/chromedriver.exe  test_selenium_petfriends.py

import time
from selenium.webdriver.common.by import By


def test_petfriends(web_browser):
    web_browser.get('https://petfriends.skillfactory.ru/')
    time.sleep(10)
    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()
    btn_exist_acc = web_browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys('studytester@gmail.com')

    # add password
    field_pass = web_browser.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys('112233')

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"