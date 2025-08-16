import os
import requests
import logging
import json
import allure
from curlify import to_curl
from contact_list_app.utils import attach


base_url = os.getenv('BASE_URL')

def send_request(method, endpoint, **kwargs) -> requests.Response:
    with allure.step(f'Отправление запроса: {method} {base_url + endpoint}'):
        response = requests.request(method=method, url=base_url + endpoint, **kwargs)
        return response

def request_logging(response: requests.Response, log_body=True, attach_curl=True):
    logging.info(f'Request method: {response.request.method}')
    logging.info(f'Request URL: {response.request.url}')
    logging.info(f'Request headers: {response.request.headers}')

    if log_body and response.request.body:
        logging.info(f'Request body: {response.request.body}')

    if attach_curl:
        curl = to_curl(response.request)
        attach.request_curl(curl)

def response_logging(response: requests.Response):
    logging.info(f'Response status code: {response.status_code}')
    logging.info(f'Response:\n{response.text}')

def response_attaching(response: requests.Response):
    try:
        attach.json_file(response)
    except json.JSONDecodeError:
        text = response.text or 'No content'
        attach.response_text(text)

def verify_status_code(response: requests.Response, status_code: int):
    with allure.step(f'Проверка соответствия кода ответа: {status_code}.'):
        assert response.status_code == status_code
