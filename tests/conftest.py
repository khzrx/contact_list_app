import os
import allure
import pytest
from dotenv import load_dotenv
from contact_list_app.utils import request
from contact_list_app.models.contact import RandomContact
from contact_list_app.models.user import RandomUser


def pytest_configure():
    load_dotenv()

@allure.title('Генерация рандомного пользователя.')
@pytest.fixture
def random_user():
    user = RandomUser()
    yield user

@allure.title('Генерация рандомного контакта.')
@pytest.fixture
def random_contact():
    contact = RandomContact()
    yield contact

@allure.title('Получение токена авторизации.')
@pytest.fixture
def authorization_token():
    payload = {
        'email': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }

    response = request.send_request(
        method='POST',
        endpoint='/users/login',
        json=payload
    )

    return response.cookies.get('token')