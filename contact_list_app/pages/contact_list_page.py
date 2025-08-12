from selene import browser, be
import allure


class ContactListPage:
    def __init__(self):
        self.logout_button = browser.element('#logout')

    @allure.step('Проверить видимость кнопки "Logout".')
    def logout_button_should_be_clickable(self):
        self.logout_button.should(be.clickable)
        return self


contact_list_page = ContactListPage()