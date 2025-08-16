import allure
import pytest
from allure_commons.types import Severity

from contact_list_app.models.contact import RandomContact
from contact_list_app.utils import request
from contact_list_app.utils import api_helper
from contact_list_app.utils.schema import validate_schema
from tests.conftest import auth_token
from contact_list_app.models.validation import AddContactValidationTexts, EditContactValidationTexts


add_contact_validation_texts = AddContactValidationTexts()
edit_contact_validation_texts = EditContactValidationTexts()

@allure.parent_suite('API')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Добавление контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Добавление контакта.')
@allure.story('Эндпоинт /contacts')
@pytest.mark.api
class TestContactAdding:

    @allure.title('POST /contacts. Успешное добавление контакта.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_add_contact_successful(self, auth_token, random_contact, delete_contacts_td):

        response = api_helper.add_contact(random_contact, auth_token)

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)


        request.verify_status_code(response, 201)
        api_helper.verify_contact_data_in_response(response, random_contact)
        validate_schema(response, 'add_contact.json')
        api_helper.verify_contact_is_in_list(response, auth_token)

    @allure.title('POST /contacts. Добавление контакта, не заполнены обязательные поля.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_add_contact_required_fields_not_filled(self, auth_token, random_contact):
        random_contact.first_name = ''
        random_contact.last_name = ''

        response = api_helper.add_contact(random_contact, auth_token)

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 400)
        api_helper.verify_error_message_in_response(response, add_contact_validation_texts.required_fields)
        validate_schema(response, 'add_contact_required_fields_not_filled.json')

@allure.parent_suite('API')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Изменение контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Изменение контакта.')
@allure.story('Эндпоинт /contacts')
@pytest.mark.api
class TestContactEditing:

    @allure.title('PUT /contacts/{id}. Успешное изменение контакта.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_edit_contact_successful(self, auth_token, random_contact, delete_contacts_td):
        new_random_contact = RandomContact()

        response = api_helper.add_contact(random_contact, auth_token)
        contact_id = response.json()['_id']
        response = api_helper.edit_contact(contact_id, new_random_contact, auth_token)

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 200)
        response = api_helper.get_contact_by_id(contact_id, auth_token)
        api_helper.verify_contact_data_in_response(response, new_random_contact)

    @allure.title('PUT /contacts/{id}. Изменение контакта, не заполнены обязательные данные.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_edit_contact_required_fields_not_filled(self, auth_token, random_contact, delete_contacts_td):
        new_random_contact = RandomContact()
        new_random_contact.first_name = ''
        new_random_contact.last_name = ''

        response = api_helper.add_contact(random_contact, auth_token)
        contact_id = response.json()['_id']
        response = api_helper.edit_contact(contact_id, new_random_contact, auth_token)

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 400)
        api_helper.verify_error_message_in_response(response, edit_contact_validation_texts.required_fields)

@allure.parent_suite('API')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Удаление контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Удаление контакта.')
@allure.story('Эндпоинт /contacts')
@pytest.mark.api
class TestContactDeleting:

    @allure.title('DELETE /contacts/{id}. Успешное удаление контакта.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_delete_contact_successful(self, auth_token, random_contact):
        response = api_helper.add_contact(random_contact, auth_token)
        contact_id = response.json()['_id']

        response = api_helper.delete_contact(contact_id, auth_token)

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 200)

        response = api_helper.get_contact_by_id(contact_id, auth_token)
        request.verify_status_code(response, 404)
