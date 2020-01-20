from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element_by_css_selector("button.btn").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    input_element = browser.find_element_by_id("input_value")
    input_value = input_element.text
    y = calc(input_value)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

