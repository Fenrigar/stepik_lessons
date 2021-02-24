from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru"
login_link_locator = "login_link"
login_user_email_locator = "[name='login-username']"
login_user_password_locator = "id_login-password"
login_submit_locator = "[name='login_submit']"
login_pup_up_text_alert = "//*[@id='login_form']//following::strong"


def test_authorization_nonexistent_login():
    try:
        # Data
        user_fake_email = "anderson@gmail.com"
        user_fake_password = "Anderson9871!"
        first_pop_up_text = "Опаньки! Мы нашли какие-то ошибки"

        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_id(login_link_locator).click()
        input_email = browser.find_element_by_css_selector(login_user_email_locator)
        input_password = browser.find_element_by_id(login_user_password_locator)

        # Act
        input_email.send_keys(user_fake_email)
        input_password.send_keys(user_fake_password)
        browser.find_element_by_css_selector(login_submit_locator).click()

        # Assert
        result_pop_up_alert = browser.find_element_by_xpath(login_pup_up_text_alert)
        assert first_pop_up_text in result_pop_up_alert.text, \
            "Appeared pop-up contains an input error authorization"

    finally:
        browser.quit()


test_authorization_nonexistent_login()
