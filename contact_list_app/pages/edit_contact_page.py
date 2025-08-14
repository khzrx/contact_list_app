from selene import browser, be, have
import allure
from contact_list_app.pages.contact_list_page import contact_list_page
from contact_list_app.utils import attach


class EditContactPage:
    def __init__(self):
        self.first_name_input = browser.element('#firstName')
        self.last_name_input = browser.element('#lastName')
        self.birthdate_input = browser.element('#birthdate')
        self.email_input = browser.element('#email')
        self.phone_input = browser.element('#phone')
        self.street_address_1_input = browser.element('#street1')
        self.street_address_2_input = browser.element('#street2')
        self.city_input = browser.element('#city')
        self.state_input = browser.element('#stateProvince')
        self.postal_code_input = browser.element('#postalCode')
        self.country_input = browser.element('#country')
        self.submit_button = browser.element('#submit')
        self.cancel_button = browser.element('#cancel')
        self.error = browser.element('#error')

    @allure.step('Очистить поле "First Name" и ввести значение.')
    def type_first_name(self, first_name: str):
        self.first_name_input.click().clear().type('')
        self.first_name_input.click().clear().type(first_name)
        return self

    @allure.step('Очистить поле "Last Name" и ввести значение.')
    def type_last_name(self, last_name: str):
        self.last_name_input.click().clear().type(last_name)
        return self

    @allure.step('Очистить поле "Date of Birth" и ввести значение.')
    def type_birthdate(self, birthdate: str):
        self.birthdate_input.click().clear().type(birthdate)
        return self

    @allure.step('Очистить поле "Email" и ввести значение.')
    def type_email(self, email: str):
        self.email_input.click().clear().type(email)
        return self

    @allure.step('Очистить поле "Phone" и ввести значение.')
    def type_phone(self, phone: str):
        self.phone_input.click().clear().type(phone)
        return self

    @allure.step('Очистить поле "Street Address 1" и ввести значение.')
    def type_street_address_1(self, address: str):
        self.street_address_1_input.click().clear().type(address)
        return self

    @allure.step('Очистить поле "Street Address 2" и ввести значение.')
    def type_street_address_2(self, address: str):
        self.street_address_2_input.click().clear().type(address)
        return self

    @allure.step('Очистить поле "City" и ввести значение.')
    def type_city(self, city: str):
        self.city_input.click().clear().type(city)
        return self

    @allure.step('Очистить поле "State or Province" и ввести значение.')
    def type_state(self, state: str):
        self.state_input.click().clear().type(state)
        return self

    @allure.step('Очистить поле "Postal Code" и ввести значение.')
    def type_postal_code(self, postal_code: str):
        self.postal_code_input.click().clear().type(postal_code)
        return self

    @allure.step('Очистить поле "Country" и ввести значение.')
    def type_country(self, country: str):
        self.country_input.click().clear().type(country)
        return self

    @allure.step('Изменить данные контакта.')
    def fill_contact_data(self, contact):
        self.type_first_name(contact.first_name)
        self.type_last_name(contact.last_name)
        self.type_birthdate(contact.birthdate)
        self.type_email(contact.email)
        self.type_phone(contact.phone)
        self.type_street_address_1(contact.street_address_1)
        self.type_street_address_2(contact.street_address_2)
        self.type_city(contact.city)
        self.type_state(contact.state)
        self.type_postal_code(contact.postal_code)
        self.type_country(contact.country)

        attach.screenshot()
        return self

    @allure.step('Кликнуть на кнопку "Submit".')
    def click_submit_button(self):
        self.submit_button.click()
        return contact_list_page

    @allure.step('Кликнуть на кнопку "Cancel".')
    def click_cancel_button(self):
        self.cancel_button.click()
        return contact_list_page

    @allure.step('Проверить текст ошибки валидации.')
    def check_validation_error_text(self, error_text: str):
        self.error.should(have.exact_text(error_text))


edit_contact_page = EditContactPage()