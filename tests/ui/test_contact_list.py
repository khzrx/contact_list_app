import allure
from allure_commons.types import Severity
from contact_list_app.pages.contact_list_page import contact_list_page
from contact_list_app.pages.add_contact_page import add_contact_page
from contact_list_app.pages.login_page import login_page
from contact_list_app.pages.contact_details_page import contact_details_page
from contact_list_app.pages.edit_contact_page import edit_contact_page
from contact_list_app.models.contact import RandomContact
from contact_list_app.models import validation

add_contact_validation_texts = validation.AddContactValidationTexts()
edit_contact_validation_texts = validation.EditContactValidationTexts()

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
    def test_add_contact_successful(self, random_contact):
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

    @allure.title('Добавление контакта, не заполнены обязательные поля.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('UI', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_add_contact_required_fields_not_filled(self):
        login_page.open()
        login_page.login()

        contact_list_page.click_add_new_contact_button()
        add_contact_page.click_submit_button()

        add_contact_page.check_validation_error_text(add_contact_validation_texts.required_fields)


@allure.parent_suite('UI')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Изменение контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Изменение контакта.')
@allure.story('Пользователь должен иметь возможность изменить данные добавленного контакта.')
class TestContactEditing:

    @allure.title('Успешное изменение всех данных контакта.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('UI', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_edit_contact_successful(self, random_contact):
        new_contact = RandomContact()
        login_page.open()
        login_page.login()
        contact_list_page.click_add_new_contact_button()
        add_contact_page.fill_contact_data(random_contact)
        add_contact_page.click_submit_button()
        contact_list_page.check_contact_was_created(random_contact)
        contact_list_page.click_on_created_contact()

        contact_details_page.click_edit_contact_button()
        edit_contact_page.fill_contact_data(new_contact)
        edit_contact_page.click_submit_button()

        contact_details_page.click_return_to_contact_list_button()
        contact_list_page.check_contact_is_not_in_list(random_contact)
        contact_list_page.check_contact_was_created(new_contact)
        contact_list_page.verify_contact_data(new_contact)

        contact_list_page.click_on_created_contact()
        contact_details_page.delete_contact()


    @allure.title('Изменение данных контакта, не заполнены обязательные поля.')
    @allure.severity(Severity.MINOR)
    @allure.tag('UI', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_edit_contact_required_fields_not_filled(self, random_contact):
        login_page.open()
        login_page.login()
        contact_list_page.click_add_new_contact_button()
        add_contact_page.fill_contact_data(random_contact)
        add_contact_page.click_submit_button()
        contact_list_page.check_contact_was_created(random_contact)
        contact_list_page.click_on_created_contact()

        contact_details_page.click_edit_contact_button()
        edit_contact_page.type_first_name('')
        edit_contact_page.type_last_name('')
        edit_contact_page.click_submit_button()

        edit_contact_page.check_validation_error_text(edit_contact_validation_texts.required_fields)

        edit_contact_page.click_cancel_button()
        contact_details_page.delete_contact()


@allure.parent_suite('UI')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Удаление контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Удаление контакта.')
@allure.story('Пользователь должен иметь возможность удалить добавленный контакт.')
class TestContactDeleting:

    @allure.title('Успешное удаление контакта.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('UI', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_delete_contact_successful(self, random_contact):
        login_page.open()
        login_page.login()
        contact_list_page.click_add_new_contact_button()
        add_contact_page.fill_contact_data(random_contact)
        add_contact_page.click_submit_button()
        contact_list_page.check_contact_was_created(random_contact)
        contact_list_page.click_on_created_contact()

        contact_details_page.delete_contact()

        contact_list_page.check_contact_is_not_in_list(random_contact)