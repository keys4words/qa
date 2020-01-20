from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	    )
	button = browser.find_element_by_id("book")
	button.click()

	input_element = browser.find_element_by_id("input_value")
	input_value = input_element.text
	y = calc(input_value)

	y_element = browser.find_element_by_id("answer")
	y_element.send_keys(y)

	# Отправляем заполненную форму
	button2 = browser.find_element_by_id("solve")
	button2.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	# time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    # browser.quit()
    pass


