import allure
import requests
from contact_list_app.models.contact import RandomContact
from contact_list_app.utils import request


@allure.step('Проверка соответствия данных созданного контакта в ответе запроса.')
def verify_contact_data_in_response(response: requests.Response, contact: RandomContact):
    response_data = response.json()
    contact_data = contact.as_dict()

    for key, value in contact_data.items():
        with allure.step(f'Проверка значения {key} на соответствие {value}'):
            assert value == response_data[key]

@allure.step('Проверка контакта в GET /contacts.')
def verify_contact_is_in_list(response: requests.Response, token: str):
    created_contact_data = response.json()

    get_contacts_response = request.send_request(
        method='GET',
        endpoint='/contacts',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert created_contact_data in get_contacts_response.json()

@allure.step('Проверка текста ошибки в ответе.')
def verify_error_message_in_response(response: requests.Response, error_message: str):
    assert response.json()['message'] == error_message

@allure.step('Добавление контакта через API.')
def add_contact(contact: RandomContact, token: str):
    payload = contact.as_dict()

    response = request.send_request(
        method='POST',
        endpoint='/contacts',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )

    return response

@allure.step('Изменение данных контакта через API по id.')
def edit_contact(contact_id: str, new_contact: RandomContact, token: str):
    payload = new_contact.as_dict()

    response = request.send_request(
        method='PUT',
        endpoint=f'/contacts/{contact_id}',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )

    return response

@allure.step('Получение данных контакта через API по id.')
def get_contact_by_id(contact_id: str, token: str):
    response = request.send_request(
        method='GET',
        endpoint=f'/contacts/{contact_id}',
        headers={'Authorization': f'Bearer {token}'}
    )

    return response

@allure.step('Удаление контакта через API по id.')
def delete_contact(contact_id: str, token: str):
    response = request.send_request(
        method='DELETE',
        endpoint=f'/contacts/{contact_id}',
        headers={'Authorization': f'Bearer {token}'}
    )

    return response