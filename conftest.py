# контент файла conftest.py

import pytest
import uuid


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # эта функция помогает обнаружить, что какой-то тест не пройден
    # эта информация передаётся разработчикам
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):
    browser = selenium
    browser.set_window_size(1400, 1000)

    # Вернуть экземпляр браузера в тест-кейс
    yield browser

    if request.node.rep_call.failed:
        # Сделать скриншот, если тест неудачный:
        try:
            browser.execute_script("document.body.bgColor='white';")
            # Сделать скриншот локальной отладки:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
        # Для удачной отладки:
            print('URL:', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)
        except:
            pass # игнорируются любые ошибки
