import allure
import pytest
from allure_commons.types import Severity
from contact_list_app.utils import request
from contact_list_app.utils.schema import validate_schema
from contact_list_app.models.validation import RegistrationValidationTexts


validation_texts = RegistrationValidationTexts()

@allure.parent_suite('API')
@allure.suite('Регистрация и авторизация')
@allure.sub_suite('Регистрация')
@allure.epic('Регистрация и авторизация')
@allure.feature('Регистрация пользователя')
@allure.story('Эндпоинт /users')
@pytest.mark.api
class TestRegistration:

    @allure.title('POST /users. Успешная регистрация пользователя.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Регистрация')
    @allure.label('owner', 'fdgoncharenko')
    def test_registration_user_successful(self, random_user):
        payload = random_user.as_dict()

        response = request.send_request(
            method='POST',
            endpoint='/users',
            json=payload
        )

        request.request_logging(response, log_body=False, attach_curl=False)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 201)

        with allure.step('Проверка ответа по значениям полей: firstName, lastName, email.'):
            assert response.json()['user']['firstName'] == random_user.first_name
            assert response.json()['user']['lastName'] == random_user.last_name
            assert response.json()['user']['email'] == random_user.email

        validate_schema(response, 'add_user.json')

    @allure.title('POST /users. Не переданы обязательные поля.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Регистрация')
    @allure.label('owner', 'fdgoncharenko')
    def test_registration_required_fields_not_filled(self, random_user):
        payload = {
            'firstName': '',
            'lastName': '',
            'email': '',
            'password': ''
        }

        response = request.send_request(
            method='POST',
            endpoint='/users',
            json=payload
        )

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 400)

        with allure.step('Проверка текста ошибки в ответе.'):
            assert response.json()['message'] == validation_texts.required_fields

