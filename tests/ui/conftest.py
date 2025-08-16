import os
import allure
import pytest
from selene.support.shared import browser
from contact_list_app.utils import attach


@allure.title('Инициализация браузера.')
@pytest.fixture(scope='function', autouse=True)
def manage_browser(request):
    browser.config.base_url = os.getenv('BASE_URL')
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.screenshot()
    attach.logs()
    attach.html()

    browser.quit()


