import allure
from allure_commons.types import Severity
from contact_list_app.pages.contact_list_page import contact_list_page
from contact_list_app.pages.add_contact_page import add_contact_page
from contact_list_app.pages.login_page import login_page
from contact_list_app.pages.contact_details_page import contact_details_page


@allure.parent_suite('UI')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Добавление контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Добавление контакта.')
@allure.story('Пользователь должен иметь возможность добавить контакт в записную книгу.')
class TestContactAdding:

    @allure.title('Успешное добавление контакта, заполнены все данные.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('UI', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_register_user_successful(self, random_contact):
        login_page.open()
        login_page.login()

        contact_list_page.click_add_new_contact_button()
        add_contact_page.fill_contact_data(random_contact)
        add_contact_page.click_submit_button()

        contact_list_page.check_contact_was_created(random_contact)
        contact_list_page.verify_contact_data(random_contact)
        contact_list_page.click_on_created_contact()
        contact_details_page.verify_contact_data(random_contact)

        contact_details_page.delete_contact()
