from selene import browser, have
import allure
from contact_list_app.utils import attach
from selenium.webdriver.support import expected_conditions as EC


class ContactDetailsPage:
    def __init__(self):
        self.edit_contact_button = browser.element('#edit-contact')
        self.delete_contact_button = browser.element('#delete')
        self.return_to_contact_list_button = browser.element('#return')
        self.first_name_field = browser.element('#firstName')
        self.last_name_field = browser.element('#lastName')
        self.birthdate_field = browser.element('#birthdate')
        self.email_field = browser.element('#email')
        self.phone_field = browser.element('#phone')
        self.street_address_1_field = browser.element('#street1')
        self.street_address_2_field = browser.element('#street2')
        self.city_field = browser.element('#city')
        self.state_field = browser.element('#stateProvince')
        self.postal_code_field = browser.element('#postalCode')
        self.country_field = browser.element('#country')

    @allure.step('Проверить данные в поле "First Name".')
    def verify_contact_first_name(self, first_name: str):
        self.first_name_field.should(have.exact_text(first_name))

    @allure.step('Проверить данные в поле "Last Name".')
    def verify_contact_last_name(self, last_name: str):
        self.last_name_field.should(have.exact_text(last_name))

    @allure.step('Проверить данные в поле "Date of Birth".')
    def verify_contact_birthdate(self, birthdate: str):
        self.birthdate_field.should(have.exact_text(birthdate))

    @allure.step('Проверить данные в поле "Email".')
    def verify_contact_email(self, email: str):
        self.email_field.should(have.exact_text(email))

    @allure.step('Проверить данные в поле "Phone".')
    def verify_contact_phone(self, phone: str | int):
        self.phone_field.should(have.exact_text(phone))

    @allure.step('Проверить данные в поле "Street Address 1".')
    def verify_contact_street_address_1(self, address: str):
        self.street_address_1_field.should(have.exact_text(address))

    @allure.step('Проверить данные в поле "Street Address 2".')
    def verify_contact_street_address_2(self, address: str):
        self.street_address_2_field.should(have.exact_text(address))

    @allure.step('Проверить данные в поле "City".')
    def verify_contact_city(self, city: str):
        self.city_field.should(have.exact_text(city))

    @allure.step('Проверить данные в поле "State or Province".')
    def verify_contact_state(self, state: str):
        self.state_field.should(have.exact_text(state))

    @allure.step('Проверить данные в поле "Postal Code".')
    def verify_contact_postal_code(self, postal_code: str):
        self.postal_code_field.should(have.exact_text(postal_code))

    @allure.step('Проверить данные в поле "Country".')
    def verify_contact_country(self, country: str):
        self.country_field.should(have.exact_text(country))

    @allure.step('Проверить данные созданного контакта на странице "Contact Details".')
    def verify_contact_data(self, contact):
        self.verify_contact_first_name(contact.first_name)
        self.verify_contact_last_name(contact.last_name)
        self.verify_contact_birthdate(contact.birthdate)
        self.verify_contact_email(contact.email)
        self.verify_contact_phone(contact.phone)
        self.verify_contact_street_address_1(contact.street_address_1)
        self.verify_contact_street_address_2(contact.street_address_2)
        self.verify_contact_city(contact.city)
        self.verify_contact_state(contact.state)
        self.verify_contact_postal_code(contact.postal_code)
        self.verify_contact_country(contact.country)
        attach.screenshot()

    @allure.step('Удалить созданный контакт')
    def delete_contact(self):
        self.delete_contact_button.click()
        browser.wait_until(EC.alert_is_present())
        browser.driver.switch_to.alert.accept()


contact_details_page = ContactDetailsPage()