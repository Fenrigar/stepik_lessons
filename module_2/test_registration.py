from sys import argv

from selenium import webdriver

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    username = browser.find_element_by_css_selector(".first_block>:nth-child(1) input")
    username.send_keys("Name")
    last_name = browser.find_element_by_css_selector(".first_block>:nth-child(2) input")
    last_name.send_keys("Lastname")
    user_email = browser.find_element_by_css_selector(".first_block>:nth-child(3) input")
    user_email.send_keys("mail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
