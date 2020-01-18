import time, math, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def answer():
    return str(math.log(int(time.time())))

urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ]



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('a_url', urls)
def test_answer(browser, a_url):
    link = f"{a_url}"
    # browser.implicitly_wait(10)
    browser.get(link)
    input_el = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")) )
    # input_el = browser.find_element_by_tag_name('textarea')
    # print(input_el.text)
    input_el.send_keys(answer())

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
    button.click()
    # message = browser.find_element_by_css_selector(".smart-hints__hint")
    message = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")) )
    print(f'----------------{message.text}---------------')
    assert "Correct!" in message.text

