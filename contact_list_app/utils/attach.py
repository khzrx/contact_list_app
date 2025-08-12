import allure
from selene import browser


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