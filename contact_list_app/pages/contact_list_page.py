from selene import browser, be, have, by
import allure
from contact_list_app.models.contact import RandomContact


class ContactListPage:
    def __init__(self):
        self.logout_button = browser.element('#logout')
        self.add_contact_button = browser.element('#add-contact')
        self.contacts = browser.all('.contactTableBodyRow')
        self.created_contact = None
        self.created_contact_fields = None

    @allure.step('Проверить видимость кнопки "Logout".')
    def logout_button_should_be_clickable(self):
        self.logout_button.should(be.clickable)
        return self

    @allure.step('Кликнуть на кнопку "Add a New Contact".')
    def click_add_new_contact_button(self):
        self.add_contact_button.click()

    @allure.step('Проверить данные в поле "Name".')
    def verify_contact_name(self, first_name: str, last_name: str):
        self.created_contact_fields[1].should(have.exact_text(f'{first_name} {last_name}'))

    @allure.step('Проверить данные в поле "Birthdate".')
    def verify_contact_birthdate(self, birthdate: str):
        self.created_contact_fields[2].should(have.exact_text(birthdate))

    @allure.step('Проверить данные в поле "Email".')
    def verify_contact_email(self, email: str):
        self.created_contact_fields[3].should(have.exact_text(email))

    @allure.step('Проверить данные в поле "Phone".')
    def verify_contact_phone(self, phone: str | int):
        self.created_contact_fields[4].should(have.exact_text(phone))

    @allure.step('Проверить данные в поле "Address".')
    def verify_contact_address(self, *args):
        self.created_contact_fields[5].should(have.exact_text(' '.join(args)))

    @allure.step('Проверить данные в поле "City, State/Province, Postal Code".')
    def verify_contact_city_state_postal(self, *args):
        self.created_contact_fields[6].should(have.exact_text(' '.join(args)))

    @allure.step('Проверить данные в поле "Country".')
    def verify_contact_country(self, country: str):
        self.created_contact_fields[7].should(have.exact_text(country))

    @allure.step('Проверить наличие созданного контакта в таблице.')
    def check_contact_was_created(self, contact: RandomContact):
        self.created_contact = browser.element(
            by.xpath(
                f'//tr[@class="contactTableBodyRow"][.//td[text()="{contact.first_name} {contact.last_name}"]]'
            )
        )

        self.created_contact_fields = self.created_contact.all('td')

    @allure.step('Проверить отсутствие контакта в таблице.')
    def check_contact_is_not_in_list(self, contact: RandomContact):
        browser.element(
            by.xpath(
                f'//tr[@class="contactTableBodyRow"][.//td[text()="{contact.first_name} {contact.last_name}"]]'
            )
        ).should(be.not_.present)

    @allure.step('Проверить данные созданного контакта в таблице.')
    def verify_contact_data(self, contact: RandomContact):
        self.verify_contact_name(contact.first_name, contact.last_name)
        self.verify_contact_birthdate(contact.birthdate)
        self.verify_contact_email(contact.email)
        self.verify_contact_phone(contact.phone)
        self.verify_contact_address(contact.street_address_1, contact.street_address_2)
        self.verify_contact_city_state_postal(contact.city, contact.state, contact.postal_code)
        self.verify_contact_country(contact.country)

    @allure.step('Перейти в "Contact Details" созданного контакта.')
    def click_on_created_contact(self):
        self.created_contact.click()


contact_list_page = ContactListPage()
