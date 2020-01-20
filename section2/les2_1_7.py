from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    chest_element = browser.find_element_by_id("treasure")
    chest_value = chest_element.get_attribute("valuex")
    y = calc(chest_value)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    input1 = browser.find_element_by_id("robotCheckbox")
    input1.click()

    input2 = browser.find_element_by_id("robotsRule")
    input2.click()
    

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

    