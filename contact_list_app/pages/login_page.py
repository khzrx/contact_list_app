import allure
from selene import browser
from contact_list_app.pages.registration_page import registration_page


class LoginPage:
    def __init__(self):
        self.email_input = browser.element('#email')
        self.password_input = browser.element('#password')
        self.submit_button = browser.element('#submit')
        self.signup_button = browser.element('#signup')

    @allure.step('Открыть страницу логина.')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Кликнуть на кнопку "Sign up".')
    def click_signup_button(self):
        self.signup_button.click()
        return registration_page


login_page = LoginPage()
