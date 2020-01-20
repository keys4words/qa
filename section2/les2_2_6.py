from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input_element = browser.find_element_by_id("input_value")
    input_value = input_element.text
    y = calc(input_value)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    input1 = browser.find_element_by_id("robotCheckbox")
    input1.click()

    browser.execute_script("window.scrollBy(0, 60);")

    input2 = browser.find_element_by_id("robotsRule")
    input2.click()
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    