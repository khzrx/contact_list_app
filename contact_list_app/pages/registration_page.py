from selene import browser, have
import allure
from contact_list_app.pages.contact_list_page import contact_list_page


class RegistrationPage:
    def __init__(self):
        self.first_name_input = browser.element('#firstName')
        self.last_name_input = browser.element('#lastName')
        self.email_input = browser.element('#email')
        self.password_input = browser.element('#password')
        self.submit_button = browser.element('#submit')
        self.cancel_button = browser.element('#cancel')
        self.error = browser.element('#error')

    @allure.step('Открыть страницу регистрации.')
    def open(self):
        browser.open('/addUser')
        return self

    @allure.step('Ввести значение в поле "First Name".')
    def type_first_name(self, first_name: str):
        self.first_name_input.type(first_name)
        return self

    @allure.step('Ввести значение в поле "Last Name".')
    def type_last_name(self, last_name: str):
        self.last_name_input.type(last_name)
        return self

    @allure.step('Ввести значение в поле "Email".')
    def type_email(self, email: str):
        self.email_input.type(email)
        return self

    def type_password(self, password: str):
        with allure.step('Ввести значение в поле "Password".'):
            self.password_input.type(password)
            return self

    @allure.step('Кликнуть на кнопку "Submit".')
    def click_submit_button(self):
        self.submit_button.click()
        return contact_list_page

    @allure.step('Проверить текст ошибки валидации.')
    def check_validation_error_text(self, error_text: str):
        self.error.should(have.exact_text(error_text))

registration_page = RegistrationPage()
