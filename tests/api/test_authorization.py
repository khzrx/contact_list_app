import os
import allure
import pytest
from allure_commons.types import Severity
from contact_list_app.utils import request
from contact_list_app.utils.schema import validate_schema


@allure.parent_suite('API')
@allure.suite('Регистрация и авторизация')
@allure.sub_suite('Авторизация')
@allure.epic('Регистрация и авторизация')
@allure.feature('Авторизация пользователя')
@allure.story('Эндпоинт /users/login')
@pytest.mark.api
class TestAuthorization:

    @allure.title('POST /users/login. Успешная авторизация.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Авторизация')
    @allure.label('owner', 'fdgoncharenko')
    def test_authorization_user_successful(self):
        payload = {
            'email': os.getenv('LOGIN'),
            'password': os.getenv('PASSWORD')
        }

        response = request.send_request(
            method='POST',
            endpoint='/users/login',
            json=payload
        )

        request.request_logging(response, log_body=False, attach_curl=False)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 200)
        validate_schema(response, 'users_login.json')


    @allure.title('POST /users/login. Логин и пароль не переданы.')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Авторизация')
    @allure.label('owner', 'fdgoncharenko')
    def test_authorization_required_fields_not_filled(self):
        payload = {
            'email': '',
            'password': ''
        }

        response = request.send_request(
            method='POST',
            endpoint='/users/login',
            json=payload
        )

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 401)

    @allure.title('POST /users/login. Передан некорректный пароль.')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Авторизация')
    @allure.label('owner', 'fdgoncharenko')
    def test_authorization_password_is_incorrect(self):
        payload = {
            'email': os.getenv('LOGIN'),
            'password': '123'
        }

        response = request.send_request(
            method='POST',
            endpoint='/users/login',
            json=payload
        )

        request.request_logging(response)
        request.response_logging(response)
        request.response_attaching(response)

        request.verify_status_code(response, 401)

