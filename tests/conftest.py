import os
import allure
import pytest
import requests
from dotenv import load_dotenv
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
@pytest.fixture(scope='module')
def auth_token(request):
    payload = {
        'email': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }

    response = requests.post(
        url=os.getenv('BASE_URL') + '/users/login',
        json=payload
    )

    return response.cookies.get('token')


@allure.title('Удаление созданных контактов после выполнения теста.')
@pytest.fixture(scope='function')
def delete_contacts_td(auth_token):
    yield

    contacts_list = requests.get(
        url=os.getenv('BASE_URL') + '/contacts',
        headers={'Authorization': f'Bearer {auth_token}'}
    ).json()

    for contact in contacts_list:
        requests.delete(
            url=os.getenv('BASE_URL') + f'/contacts/{contact["_id"]}',
            headers={'Authorization': f'Bearer {auth_token}'}
        )
