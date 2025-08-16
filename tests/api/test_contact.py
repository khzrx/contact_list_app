import allure
import pytest
from allure_commons.types import Severity
from contact_list_app.utils import request
from contact_list_app.utils import api_helper
from contact_list_app.utils.schema import validate_schema
from tests.conftest import auth_token


# validation_texts = RegistrationValidationTexts()

@allure.parent_suite('API')
@allure.suite('Добавление, изменение, удаление контактов.')
@allure.sub_suite('Добавление контакта.')
@allure.epic('Добавление, изменение, удаление контактов.')
@allure.feature('Добавление контакта.')
@allure.story('Эндпоинт /contacts')
@pytest.mark.api
class TestRegistration:

    @allure.title('POST /contacts. Успешное добавление контакта.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Контакты')
    @allure.label('owner', 'fdgoncharenko')
    def test_add_contact_successful(self, auth_token, random_contact, delete_contacts_after_test):
        payload = random_contact.as_dict()

        response = request.send_request(
            method='POST',
            endpoint='/contacts',
            json=payload,
            headers={'Authorization': f'Bearer {auth_token}'}
        )

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)


        request.verify_status_code(response, 201)
        api_helper.verify_contact_data_in_response(response, random_contact)
        validate_schema(response, 'add_contact.json')
        api_helper.verify_contact_is_in_list(response, auth_token)


