import os
import allure
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

def add_video(browser):
    selenoid_url = os.getenv('SELENOID_URL')
    video_url = f'https://{selenoid_url}/video/' + browser.driver.session_id + '.mp4'
    video_html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"

    allure.attach(
        body=video_html,
        name='video_' + browser.driver.session_id,
        attachment_type= allure.attachment_type.HTML,
        extension='.html'
    )