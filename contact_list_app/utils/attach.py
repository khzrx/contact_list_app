import allure
from curlify import to_curl
from requests import Response
from selene import browser
import json


def screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )

def xml():
    allure.attach(
        browser.driver.page_source,
        name='xml_dump',
        attachment_type=allure.attachment_type.XML,
        extension='.xml'
    )

def html():
    allure.attach(
        browser.driver.page_source,
        name='html_dump',
        attachment_type=allure.attachment_type.HTML,
        extension='.txt'
    )

def logs():
    log = ''.join(f'{text}\n' for text in browser.driver.execute('getLog', {'type': 'browser'})['value'])

    allure.attach(
        log,
        name='browser_logs',
        attachment_type=allure.attachment_type.HTML,
        extension='.log'
    )

def request_curl(curl):
    allure.attach(
        body=curl,
        name=curl,
        attachment_type=allure.attachment_type.TEXT,
        extension='.txt'
    )

def json_file(response):
    allure.attach(
        body=json.dumps(response.json(), indent=4),
        name='response',
        attachment_type=allure.attachment_type.JSON,
        extension='json'
    )

def response_text(text):
    allure.attach(
        body=text,
        name='response',
        attachment_type=allure.attachment_type.TEXT,
        extension='.txt'
    )