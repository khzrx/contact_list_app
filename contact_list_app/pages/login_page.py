import os
import allure
from selene import browser, have
from contact_list_app.pages.registration_page import registration_page


class LoginPage:
    def __init__(self):
        self.email_input = browser.element('#email')
        self.password_input = browser.element('#password')
        self.submit_button = browser.element('#submit')
        self.signup_button = browser.element('#signup')
        self.error = browser.element('#error')

    @allure.step('Открыть страницу логина.')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Кликнуть на кнопку "Sign up".')
    def click_signup_button(self):
        self.signup_button.click()
        return registration_page

    @allure.step('Ввести email.')
    def type_email(self):
        self.email_input.type(os.getenv('LOGIN'))
        return self

    @allure.step('Ввести пароль.')
    def type_password(self):
        self.password_input.type(os.getenv('PASSWORD'))
        return self

    @allure.step('Кликнуть на кнопку "Submit".')
    def click_submit_button(self):
        self.submit_button.click()
        return registration_page

    @allure.step('Авторизоваться на сайте.')
    def login(self):
        self.type_email()
        self.type_password()
        self.click_submit_button()

    @allure.step('Проверить текст ошибки валидации.')
    def check_validation_error_text(self, error_text: str):
        self.error.should(have.exact_text(error_text))


login_page = LoginPage()
